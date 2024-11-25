import { get, post } from "../helpers";
import { LocalStorage } from "../localStorage";
import type { Entity } from "./entity";

export interface Mix {
    id: number;
    project_id: number;
    created_at: string;
    description: string;
    name: string;
}

export type MixCreate = Omit<Mix, 'id' | 'created_at'>;

class MixEntity implements Entity<Mix> {
    async getAll(): Promise<Mix[]> {
        const response = await get(`/mixes/${LocalStorage.CurrentProjectId.get()}`);
        return await response.json() as Mix[];
    }

    async create(data: MixCreate): Promise<Mix> {
        const response = await post('/mixes', data);
        return await response.json();
    }

    async delete(id: number): Promise<void> {
        await get(`/mixes/delete/${id}`);
    }

    async update(id: number, data: MixCreate): Promise<Mix> {
        const response = await post(`/mixes/update/${id}`, data);
        return await response.json() as Mix;
    }

    async get(id: number): Promise<Mix> {
        const response = await get(`/mixes/${LocalStorage.CurrentProjectId.get()}/${id}`);
        return await response.json() as Mix;
    }
}

const MixEntityInstance = new MixEntity();
Object.freeze(MixEntityInstance);
export default MixEntityInstance;