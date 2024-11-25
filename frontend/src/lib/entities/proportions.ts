import { get, post } from "../helpers";
import { LocalStorage } from "../localStorage";
import { Entity } from "./entity";

export interface Proportion {
    id: number;
    mix_id: number;
    material_id: number;
    quantity: number;
    unit_id: number;
}

export type ProportionCreate = Omit<Proportion, 'id'>;

class ProportionEntity extends Entity<Proportion> {
    async getAll(): Promise<Proportion[]> {
        const mixId = LocalStorage.CurrentMixId.get();
        const response = await get(`/proportions/${mixId}`);
        return await response.json() as Proportion[];
    }

    async create(data: ProportionCreate): Promise<Proportion> {
        const response = await post('/proportions', data);
        return await response.json();
    }

    async delete(id: number): Promise<void> {
        await get(`/proportions/delete/${id}`);
    }

    async update(id: number, data: ProportionCreate): Promise<Proportion> {
        const response = await post(`/proportions/update/${id}`, data);
        return await response.json();
    }

    async get(id: number): Promise<Proportion> {
        const mixId = LocalStorage.CurrentMixId.get();
        const response = await get(`/proportions/${mixId}/${id}`);
        return await response.json();
    }
}

const ProportionEntityInstance = new ProportionEntity();
Object.freeze(ProportionEntityInstance);
export default ProportionEntityInstance;