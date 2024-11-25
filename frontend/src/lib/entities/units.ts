import { get } from "../helpers";

interface Unit {
    id: number;
    name: string;
    symbol: string;
}

export async function getAllUnits(): Promise<Unit[]> {
    return await (await get('/units')).json() as Unit[];
}
