import { get, post } from "../helpers";
import { LocalStorage } from "../localStorage";
import type { Entity } from "./entity";

export interface Project {
    id: number;
    user_id: number;
    created_at: string;
    description: string;
    name: string;
    start_date?: string;
    end_date?: string;
}

export type ProjectCreate = Omit<Project, 'id' | 'created_at'>;

export class ProjectEntity implements Entity<Project> {
    async getAll(): Promise<Project[]> {
        const user_id = LocalStorage.CurrentUserId.get();
        const response = await get(`/projects/${user_id}`);
        return await response.json() as Project[];
    }

    async get(id: number): Promise<Project> {
        const user_id = LocalStorage.CurrentUserId.get();
        const response = await get(`/projects/${user_id}/${id}`);
        return await response.json();
    }

    async create(data: ProjectCreate): Promise<Project> {
        const response = await post("/projects", data);
        return await response.json();
    }

    async delete(id: number): Promise<void> {
        await get(`/projects/delete/${id}`);
    }

    async update(id: number, data: ProjectCreate): Promise<Project> {
        const user_id = LocalStorage.CurrentUserId.get();
        const response = await post(`/projects/update/${id}`, data);
        return await response.json();
    }
}

const ProjectEntityInstance = new ProjectEntity();
Object.freeze(ProjectEntityInstance);
export default ProjectEntityInstance;