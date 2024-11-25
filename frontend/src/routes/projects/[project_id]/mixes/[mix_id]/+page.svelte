<script lang="ts">
    import { goto } from "$app/navigation";
    import { page } from "$app/stores";
    import MaterialEntityInstance, {
        type Material,
    } from "$lib/entities/materials";
    import ProportionEntityInstance, {
        type Proportion,
    } from "$lib/entities/proportions";
    import TestResultEntityInstance, {
        type TestResult,
    } from "$lib/entities/test-results";
    import { onMount } from "svelte";
    import Center from "../../../../../components/center.svelte";
    import Header from "../../../../../components/header.svelte";
    import Squeeze from "../../../../../components/squeeze.svelte";
    import { LocalStorage } from "$lib/localStorage";
    import {
        Button,
        Table,
        TableBody,
        TableBodyCell,
        TableBodyRow,
        TableHead,
        TableHeadCell,
    } from "flowbite-svelte";
    import { PlusOutline, TrashBinOutline } from "flowbite-svelte-icons";
    import { formatDate } from "$lib/helpers";

    let materialsWithProportions: (Material & { proportion: Proportion })[] =
        $state([]);
    async function getMaterialProportions() {
        const materials = await MaterialEntityInstance.getAll();
        const proportions = await ProportionEntityInstance.getAll();

        materialsWithProportions = materials.map((material: Material) => {
            const proportion = proportions.find(
                (proportion: Proportion) =>
                    proportion.material_id === material.id,
            ) as unknown as Proportion;

            return {
                ...material,
                proportion,
            };
        });
    }

    let testResults: TestResult[] = $state([]);
    async function getTestResults() {
        testResults = await TestResultEntityInstance.getAll();
    }

    onMount(() => {
        const sub = page.subscribe(async (value) => {
            const { mix_id } = value.params;
            LocalStorage.CurrentMixId.set(mix_id);
            getMaterialProportions();
            getTestResults();
        });
        sub();
    });
</script>

<Header></Header>

<Center>
    <Squeeze>
        <div class="w-full flex justify-between">
            <h1>Materials</h1>
            <button onclick={() => goto("/create-material")}>
                <PlusOutline class="h-10 w-10"></PlusOutline>
            </button>
        </div>
        <div class="flex flex-col">
            <Table class="table-fixed">
                <TableHead class="bg-slate-200">
                    <TableHeadCell>NAME</TableHeadCell>
                    <TableHeadCell>AMOUNT</TableHeadCell>
                    <TableHeadCell>COST PER UNIT</TableHeadCell>
                    <TableHeadCell></TableHeadCell>
                </TableHead>
                <TableBody tableBodyClass="divide-y divide-slate-200">
                    {#each materialsWithProportions as material}
                        <TableBodyRow class="bg-slate-600 p-2">
                            <TableBodyCell class="text-center text-slate-100"
                                >{material.name}</TableBodyCell
                            >
                            <TableBodyCell class="text-center text-slate-100"
                                >{material.proportion?.quantity}</TableBodyCell
                            >
                            <TableBodyCell class="text-center text-slate-100"
                                >{material.cost_per_unit}</TableBodyCell
                            >
                            <TableBodyCell tdClass="flex justify-end">
                                <Button
                                    class="flex gap-2 text-slate-100 p-2"
                                    onclick={(e: any) => {
                                        e.preventDefault();
                                        e.stopPropagation();
                                        ProportionEntityInstance.delete(
                                            Number(material.proportion.id),
                                        );
                                        MaterialEntityInstance.delete(
                                            Number(material.id),
                                        );

                                        materialsWithProportions =
                                            materialsWithProportions.filter(
                                                (m) => m.id !== material.id,
                                            );
                                    }}
                                >
                                    Delete
                                    <TrashBinOutline
                                        class="h-6 w-6 text-slate-100"
                                    ></TrashBinOutline>
                                </Button>
                            </TableBodyCell>
                        </TableBodyRow>
                    {/each}
                </TableBody>
            </Table>
        </div>
        <div class="w-full flex justify-between">
            <h1>Test Result</h1>
            <button onclick={() => goto("/create-test-result")}>
                <PlusOutline class="h-10 w-10"></PlusOutline>
            </button>
        </div>
        <Table class="table-fixed">
            <TableHead class="bg-slate-200">
                <TableHeadCell>PROPERTY MEASURED</TableHeadCell>
                <TableHeadCell>RESULT</TableHeadCell>
                <TableHeadCell>TEST DATE</TableHeadCell>
                <TableHeadCell></TableHeadCell>
            </TableHead>
            <TableBody tableBodyClass="divide-y divide-slate-200">
                {#each testResults as testResult}
                    <TableBodyRow class="bg-slate-600 p-2">
                        <TableBodyCell class="text-center text-slate-100"
                            >{testResult.property_measured}</TableBodyCell
                        >
                        <TableBodyCell class="text-center text-slate-100"
                            >{testResult.result}</TableBodyCell
                        >
                        <TableBodyCell class="text-center text-slate-100"
                            >{formatDate(testResult.test_date)}</TableBodyCell
                        >
                        <TableBodyCell tdClass="flex justify-end">
                            <Button
                                class="flex gap-2 text-slate-100 p-2"
                                onclick={(e: any) => {
                                    e.preventDefault();
                                    e.stopPropagation();
                                    TestResultEntityInstance.delete(
                                        Number(testResult.id),
                                    );
                                    testResults = testResults.filter(
                                        (t) => t.id !== testResult.id,
                                    );
                                }}
                            >
                                Delete
                                <TrashBinOutline class="h-6 w-6 text-slate-100"
                                ></TrashBinOutline>
                            </Button>
                        </TableBodyCell>
                    </TableBodyRow>
                {/each}
            </TableBody>
        </Table>
    </Squeeze>
</Center>
