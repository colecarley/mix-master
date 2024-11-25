from decimal import Decimal
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import entities.user as User, database, entities.project as Project, entities.mix as Mix, entities.proportion as Proportion, entities.material as Material, entities.unit as Unit, entities.testResult as TestResult
from pydantic import BaseModel, Field, condecimal
from datetime import date

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

class UserCreate(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str

@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(database.get_db)):
    user = User.User(username=user.username, password=user.password, first_name=user.first_name, last_name=user.last_name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.post("/users/update/{user_id}")
def update_user(user_id, user: UserCreate, db: Session = Depends(database.get_db)):
    old_user = db.query(User.User).filter(User.User.id == user_id).first()
    old_user.username = user.username
    old_user.password = user.password
    old_user.first_name = user.first_name
    old_user.last_name = user.last_name
    db.commit()
    return old_user

class ProjectCreate(BaseModel):
    name: str
    description: str
    user_id: int # should this be provided by the frontend?
    start_date: str 
    end_date: str

@app.post("/projects/")
def create_project(project: ProjectCreate, db: Session = Depends(database.get_db)):
    print(project)
    project = Project.Project(name=project.name, 
                                description=project.description,
                                user_id=project.user_id,
                                created_at=date.today().isoformat(),
                                start_date=project.start_date,
                                end_date=project.end_date)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

@app.post("/projects/update/{project_id}")
def update_project(project_id, project: ProjectCreate, db: Session = Depends(database.get_db)):
    old_project = db.query(Project.Project).filter(Project.Project.id == project_id).first()
    old_project.name = project.name
    old_project.description = project.description
    old_project.start_date = project.start_date
    old_project.end_date = project.end_date
    db.commit()
    return old_project

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(database.get_db)):
    user = db.query(User.User).filter(User.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/projects/{user_id}")
def read_project(user_id, db: Session = Depends(database.get_db)):
    project = list(db.query(Project.Project).filter(Project.Project.user_id == user_id))
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@app.get("/projects/delete/{project_id}")
def delete_project(project_id, db: Session = Depends(database.get_db)):
    project = db.query(Project.Project).filter(Project.Project.id == project_id).first()
    db.delete(project)
    db.commit()
    return project

@app.get("/projects/{user_id}/{project_id}")
def read_project(user_id, project_id, db: Session = Depends(database.get_db)):
    project = db.query(Project.Project).filter(Project.Project.user_id == user_id, Project.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

class Login(BaseModel):
    username: str
    password: str

@app.post("/login/")
def login(login: Login, db: Session = Depends(database.get_db)):
    user = db.query(User.User).filter(User.User.username == login.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.password != login.password:
        raise HTTPException(status_code=401, detail="Invalid password")

    return user


@app.post("/signup/")
def signup(user: UserCreate, db: Session = Depends(database.get_db)):
    user = User.User(username=user.username, password=user.password, first_name=user.first_name, last_name=user.last_name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.get("/mixes/{project_id}")
def read_mixes(project_id, db: Session = Depends(database.get_db)):
    mixes = list(db.query(Mix.Mix).filter(Mix.Mix.project_id == project_id))
    return mixes


class MixCreate(BaseModel):
    project_id: int
    description: str
    name: str

@app.post("/mixes/")
def create_mix(mix: MixCreate, db: Session = Depends(database.get_db)):
    mix = Mix.Mix(project_id=mix.project_id, description=mix.description, name=mix.name, created_at=date.today().isoformat())
    db.add(mix)
    db.commit()
    db.refresh(mix)
    return mix

@app.post("/mixes/update/{mix_id}")
def update_mix(mix_id, mix: MixCreate, db: Session = Depends(database.get_db)):
    old_mix = db.query(Mix.Mix).filter(Mix.Mix.id == mix_id).first()
    old_mix.name = mix.name
    old_mix.description = mix.description
    db.commit()
    return old_mix

@app.get("/mixes/delete/{mix_id}")
def delete_mix(mix_id, db: Session = Depends(database.get_db)):
    mix = db.query(Mix.Mix).filter(Mix.Mix.id == mix_id).first()
    if not mix:
        raise HTTPException(status_code=404, detail="Mix not found")
    db.delete(mix)
    db.commit()
    return mix

@app.get("/mixes/{project_id}/{mix_id}")
def read_mix(project_id, mix_id, db: Session = Depends(database.get_db)):
    mix = db.query(Mix.Mix).filter(Mix.Mix.project_id == project_id, Mix.Mix.id == mix_id).first()
    if not mix:
        raise HTTPException(status_code=404, detail="Mix not found")
    return mix

class MaterialCreate(BaseModel):
    mix_id: int
    name: str
    cost_per_unit: int
    unit_id: int

@app.post("/materials/")
def create_material(material: MaterialCreate, db: Session = Depends(database.get_db)):
    material = Material.Material(mix_id=material.mix_id, name=material.name, cost_per_unit=material.cost_per_unit, unit_id=material.unit_id)
    db.add(material)
    db.commit()
    db.refresh(material)
    return material

@app.post("/materials/update/{material_id}")
def update_material(material_id, material: MaterialCreate, db: Session = Depends(database.get_db)):
    old_material = db.query(Material.Material).filter(Material.Material.id == material_id).first()
    old_material.name = material.name
    old_material.cost_per_unit = material.cost_per_unit
    db.commit()
    return material

@app.get("/materials/{mix_id}")
def get_materials(mix_id, db: Session = Depends(database.get_db)):
    materials = list(db.query(Material.Material).filter(Material.Material.mix_id == mix_id))
    return materials

@app.get("/materials/delete/{material_id}")
def delete_material(material_id, db: Session = Depends(database.get_db)):
    material = db.query(Material.Material).filter(Material.Material.id == material_id).first()
    if not material:
        raise HTTPException(status_code=404, detail="Material not found")
    db.delete(material)
    db.commit()
    return material

@app.get("/materials/{mix_id}/{material_id}")
def get_material(mix_id, material_id, db: Session = Depends(database.get_db)):
    material = db.query(Material.Material).filter(Material.Material.mix_id == mix_id, Material.Material.id == material_id).first()
    if not material:
        raise HTTPException(status_code=404, detail="Material not found")
    return material

class ProportionCreate(BaseModel):
    mix_id: int
    material_id: int
    quantity: int
    unit_id: int

@app.post("/proportions/")
def create_proportion(proportion: ProportionCreate, db: Session = Depends(database.get_db)):
    proportion = Proportion.Proportion(mix_id=proportion.mix_id, material_id=proportion.material_id, quantity=proportion.quantity, unit_id=proportion.unit_id)
    db.add(proportion)
    db.commit()
    db.refresh(proportion)
    return proportion

@app.post("/proportions/update/{proportion_id}")
def update_proportion(proportion_id, proportion: ProportionCreate, db: Session = Depends(database.get_db)):
    old_proportion = db.query(Proportion.Proportion).filter(Proportion.Proportion.id == proportion_id).first()
    old_proportion.quantity = proportion.quantity
    old_proportion.unit_id = proportion.unit_id
    db.commit()
    return proportion

@app.get("/proportions/{mix_id}")
def get_proportions(mix_id, db: Session = Depends(database.get_db)):
    proportions = list(db.query(Proportion.Proportion).filter(Proportion.Proportion.mix_id == mix_id))
    return proportions

@app.get("/proportions/delete/{proportion_id}")
def delete_proportion(proportion_id, db: Session = Depends(database.get_db)):
    proportion = db.query(Proportion.Proportion).filter(Proportion.Proportion.id == proportion_id).first()
    if not proportion:
        raise HTTPException(status_code=404, detail="Proportion not found")
    db.delete(proportion)
    db.commit()
    return proportion

@app.get("/proportions/{mix_id}/{proportion_id}")
def get_proportion(mix_id, proportion_id, db: Session = Depends(database.get_db)):
    proportion = db.query(Proportion.Proportion).filter(Proportion.Proportion.mix_id == mix_id, Proportion.Proportion.id == proportion_id).first()
    if not proportion:
        raise HTTPException(status_code=404, detail="Proportion not found")
    return proportion

@app.get("/units")
def get_units(db: Session = Depends(database.get_db)):
    units = list(db.query(Unit.Unit).all())
    return units

class TestResultCreate(BaseModel):
    mix_id: int
    test_date: str
    property_measured: str
    result: int
    unit_id: int

@app.post("/test-results")
def create_test_result(test_result: TestResultCreate, db: Session = Depends(database.get_db)):
    test_result = TestResult.TestResult(mix_id=test_result.mix_id, test_date=test_result.test_date, property_measured=test_result.property_measured, result=test_result.result, unit_id=test_result.unit_id)
    db.add(test_result)
    db.commit()
    db.refresh(test_result)
    return test_result

@app.post("/test-results/update/{test_result_id}")
def update_test_result(test_result_id, test_result: TestResultCreate, db: Session = Depends(database.get_db)):
    old_test_result = db.query(TestResult.TestResult).filter(TestResult.TestResult.id == test_result_id).first()

    old_test_result.test_date = test_result.test_date
    old_test_result.result = test_result.result
    old_test_result.property_measured = test_result.property_measured
    old_test_result.unit_id = test_result.unit_id
    db.commit()
    return old_test_result

@app.get("/test-results/{mix_id}")
def get_test_results(mix_id, db: Session = Depends(database.get_db)):
    test_results = list(db.query(TestResult.TestResult).filter(TestResult.TestResult.mix_id == mix_id))
    return test_results

@app.get("/test-results/delete/{test_result_id}")
def delete_test_result(test_result_id, db: Session = Depends(database.get_db)):
    test_result = db.query(TestResult.TestResult).filter(TestResult.TestResult.id == test_result_id).first()
    if not test_result:
        raise HTTPException(status_code=404, detail="Test result not found")
    db.delete(test_result)
    db.commit()
    return test_result

@app.get("/test-results/{mix_id}/{test_result_id}")
def get_test_result(mix_id, test_result_id, db: Session = Depends(database.get_db)):
    test_result = db.query(TestResult.TestResult).filter(TestResult.TestResult.mix_id == mix_id, TestResult.TestResult.id == test_result_id).first()
    if not test_result:
        raise HTTPException(status_code=404, detail="Test result not found")
    return test_result