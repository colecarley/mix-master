import { get, post } from "../helpers";
import { LocalStorage } from "../localStorage";
import type { Entity } from "./entity";

export interface Material {
    id: number;
    mix_id: number;
    name: string;
    cost_per_unit: number;
    unit_id: number;
}

export type MaterialCreate = Omit<Material, 'id'>;

class MaterialEntity implements Entity<Material> {
    async getAll(): Promise<Material[]> {
        const mixId = LocalStorage.CurrentMixId.get();
        const response = await get(`/materials/${mixId}`);
        return await response.json() as Material[];
    }

    async create(data: MaterialCreate): Promise<Material> {
        const response = await post('/materials', data);
        return await response.json() as Material;
    }

    async delete(id: number): Promise<void> {
        await get(`/materials/delete/${id}`);
    }

    async update(id: number, data: MaterialCreate): Promise<Material> {
        const response = await post(`/materials/update/${id}`, data);
        return await response.json() as Material;
    }

    async get(id: number): Promise<Material> {
        const mixId = LocalStorage.CurrentMixId.get();
        const response = await get(`/materials/${mixId}/${id}`);
        return await response.json() as Material;
    }
}

const MaterialEntityInstance = new MaterialEntity();
Object.freeze(MaterialEntityInstance);
export default MaterialEntityInstance;