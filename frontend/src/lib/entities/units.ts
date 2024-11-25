import { get } from "../helpers";

interface Unit {
    id: number;
    name: string;
    symbol: string;
}

export async function getAllUnits(): Promise<Unit[]> {
    return await (await get('/units')).json() as Unit[];
}

export async function getUnit(id: number): Promise<Unit> {
    return await (await get(`/units/${id}`)).json() as Unit;
}