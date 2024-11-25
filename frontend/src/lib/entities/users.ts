import { get, post } from "$lib/helpers";
import { Entity } from "./entity";

export interface User {
    id: number;
    first_name: string;
    last_name: string;
    username: string;
    password: string;
}

export type UserCreate = Omit<User, 'id'>;

class UserEntity extends Entity<User> {
    async getAll(): Promise<User[]> {
        throw new Error('Not implemented');
    }

    async create(data: UserCreate): Promise<User> {
        const response = await post('/users', data);
        return await response.json();
    }

    async delete(id: number): Promise<void> {
        await get(`/users/delete/${id}`);
    }

    async update(id: number, data: UserCreate): Promise<User> {
        const response = await post(`/users/update/${id}`, data);
        return await response.json();
    }

    async get(_: number): Promise<User> {
        throw new Error('Not implemented');
    }
}

const UserEntityInstance = new UserEntity();
Object.freeze(UserEntityInstance);
export default UserEntityInstance;
