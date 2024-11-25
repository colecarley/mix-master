import { get, post } from "../helpers";
import { LocalStorage } from "../localStorage";
import type { Entity } from "./entity";

export interface TestResult {
    id: number;
    mix_id: number;
    test_date: string;
    property_measured: string;
    result: number;
    unit_id: number;
}

export type TestResultCreate = Omit<TestResult, 'id'>;

class TestResultEntity implements Entity<TestResult> {
    async getAll(): Promise<TestResult[]> {
        const mixId = LocalStorage.CurrentMixId.get();
        const response = await get(`/test-results/${mixId}`);
        return await response.json() as TestResult[];
    }

    async create(data: TestResultCreate): Promise<TestResult> {
        const response = await post('/test-results', data);
        return await response.json();
    }

    async delete(id: number): Promise<void> {
        await get(`/test-results/delete/${id}`);
    }

    async update(id: number, data: TestResultCreate): Promise<TestResult> {
        const response = await post(`/test-results/update/${id}`, data);
        return await response.json();
    }

    async get(id: number): Promise<TestResult> {
        const mixId = LocalStorage.CurrentMixId.get();
        const response = await get(`/test-results/${mixId}/${id}`);
        return await response.json();
    }
}

const TestResultEntityInstance = new TestResultEntity();
Object.freeze(TestResultEntityInstance);
export default TestResultEntityInstance;