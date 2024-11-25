

export abstract class Entity<T> {
    abstract getAll(): Promise<T[]>;
    abstract get(id: number): Promise<T>;
    abstract create(data: T): Promise<T>;
    abstract delete(id: number): Promise<void>;
    abstract update(id: number, data: T): Promise<T>;
}