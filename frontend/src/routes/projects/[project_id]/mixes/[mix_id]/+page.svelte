<script lang="ts">
    import { goto } from "$app/navigation";
    import { page } from "$app/stores";
    import MaterialEntityInstance, {
        type Material,
    } from "$lib/entities/materials";
    import MixEntityInstance, { type Mix } from "$lib/entities/mixes";
    import ProportionEntityInstance, {
        type Proportion,
    } from "$lib/entities/proportions";
    import TestResultEntityInstance, {
        type TestResult,
    } from "$lib/entities/test-results";
    import { formatDate } from "$lib/helpers";
    import { LocalStorage } from "$lib/localStorage";
    import {
        Button,
        TabItem,
        Table,
        TableBody,
        TableBodyCell,
        TableBodyRow,
        TableHead,
        TableHeadCell,
        Tabs,
    } from "flowbite-svelte";
    import {
        EditOutline,
        PlusOutline,
        TrashBinOutline,
    } from "flowbite-svelte-icons";
    import { onMount } from "svelte";
    import Center from "../../../../../components/center.svelte";
    import Header from "../../../../../components/header.svelte";
    import MmCard from "../../../../../components/mm-card.svelte";
    import Squeeze from "../../../../../components/squeeze.svelte";
    import { getUnit } from "$lib/entities/units";

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

    let mix: Mix | null = $state(null);
    async function getMix() {
        mix = await MixEntityInstance.get(
            Number(LocalStorage.CurrentMixId.get()),
        );
    }

    onMount(() => {
        const sub = page.subscribe(async (value) => {
            const { mix_id } = value.params;
            LocalStorage.CurrentMixId.set(mix_id);
            getMix();
            getMaterialProportions();
            getTestResults();
        });
        sub();
    });
</script>

<Center>
    <Header></Header>
    <Squeeze>
        {#if mix}
            <Tabs tabStyle="pill">
                <TabItem
                    title="Mix"
                    open
                    activeClasses="p-4 text-white rounded-xl bg-primary shadow-xl text-lg"
                    inactiveClasses="p-4 rounded-xl text-lg bg-white text-primary"
                >
                    <h1 class="text-gray-600">Mix</h1>
                    <div class="mb-6">
                        <MmCard
                            title={mix.name}
                            subtitle={formatDate(mix.created_at)}
                            description={mix.description}
                            onUpdate={() => {
                                if (!mix) {
                                    return;
                                }
                                goto(`/update-mix/${mix.id}`);
                            }}
                        ></MmCard>
                    </div>
                    <div class="flex justify-end">
                        <Button
                            class="bg-primary flex gap-2"
                            onclick={() => {
                                if (!mix) {
                                    return;
                                }
                                MixEntityInstance.delete(Number(mix.id));

                                goto(`/projects/${mix.project_id}`);
                            }}
                        >
                            <TrashBinOutline class="h-4 w-4"></TrashBinOutline>
                            Delete
                        </Button>
                    </div>
                </TabItem>
                <TabItem
                    title="Materials"
                    activeClasses="p-4 text-white rounded-xl bg-primary shadow-xl text-lg"
                    inactiveClasses="p-4 rounded-xl text-lg bg-white text-primary"
                >
                    <div class="w-full flex justify-between">
                        <h1 class="text-gray-600">Materials</h1>
                        <button onclick={() => goto("/create-material")}>
                            <PlusOutline class="h-10 w-10 text-gray-600"
                            ></PlusOutline>
                        </button>
                    </div>
                    <div class="flex flex-col">
                        <Table class="table-fixed shadow-xl">
                            <TableHead class="bg-primary text-white">
                                <TableHeadCell class="p-2">NAME</TableHeadCell>
                                <TableHeadCell>AMOUNT</TableHeadCell>
                                <TableHeadCell>COST PER UNIT</TableHeadCell>
                                <TableHeadCell></TableHeadCell>
                            </TableHead>
                            <TableBody
                                tableBodyClass="divide-y divide-slate-200"
                            >
                                {#each materialsWithProportions as material}
                                    <TableBodyRow class="p-2">
                                        <TableBodyCell class="text-center"
                                            >{material.name}</TableBodyCell
                                        >
                                        <TableBodyCell class="text-center"
                                            >{material.proportion?.quantity}
                                            {#await getUnit(material.proportion?.unit_id) then unit}
                                                {unit.symbol}
                                            {/await}
                                        </TableBodyCell>
                                        <TableBodyCell class="text-center"
                                            >{material.cost_per_unit}
                                            {#await getUnit(material.unit_id) then unit}
                                                {unit.symbol}
                                            {/await}</TableBodyCell
                                        >
                                        <TableBodyCell
                                            tdClass="flex justify-end gap-6"
                                        >
                                            <Button
                                                class="flex gap-2 text-gray-600 p-2"
                                                onclick={(e: any) => {
                                                    e.preventDefault();
                                                    e.stopPropagation();
                                                    goto(
                                                        `/update-material/${material.id}/${material.proportion?.id}`,
                                                    );
                                                }}
                                            >
                                                Update
                                                <EditOutline class="h-6 w-6"
                                                ></EditOutline>
                                            </Button>
                                            <Button
                                                class="flex gap-2 text-gray-600 p-2"
                                                onclick={(e: any) => {
                                                    e.preventDefault();
                                                    e.stopPropagation();
                                                    ProportionEntityInstance.delete(
                                                        Number(
                                                            material.proportion
                                                                .id,
                                                        ),
                                                    );
                                                    MaterialEntityInstance.delete(
                                                        Number(material.id),
                                                    );

                                                    materialsWithProportions =
                                                        materialsWithProportions.filter(
                                                            (m) =>
                                                                m.id !==
                                                                material.id,
                                                        );
                                                }}
                                            >
                                                Delete
                                                <TrashBinOutline class="h-6 w-6"
                                                ></TrashBinOutline>
                                            </Button>
                                        </TableBodyCell>
                                    </TableBodyRow>
                                {/each}
                            </TableBody>
                        </Table>
                    </div>
                </TabItem>
                <TabItem
                    title="Test Results"
                    activeClasses="p-4 text-white rounded-xl bg-primary shadow-xl text-lg"
                    inactiveClasses="p-4 rounded-xl text-lg bg-white text-primary"
                >
                    <div class="w-full flex justify-between">
                        <h1 class="text-gray-600">Test Results</h1>
                        <button onclick={() => goto("/create-test-result")}>
                            <PlusOutline class="h-10 w-10 text-gray-600"
                            ></PlusOutline>
                        </button>
                    </div>
                    <Table class="table-fixed shadow-xl ">
                        <TableHead class="bg-primary text-white">
                            <TableHeadCell class="p-2"
                                >PROPERTY MEASURED</TableHeadCell
                            >
                            <TableHeadCell>RESULT</TableHeadCell>
                            <TableHeadCell>TEST DATE</TableHeadCell>
                            <TableHeadCell></TableHeadCell>
                        </TableHead>
                        <TableBody tableBodyClass="divide-y divide-slate-200">
                            {#each testResults as testResult}
                                <TableBodyRow class="p-2">
                                    <TableBodyCell class="text-center"
                                        >{testResult.property_measured}</TableBodyCell
                                    >
                                    <TableBodyCell class="text-center">
                                        {testResult.result}
                                        {#await getUnit(testResult.unit_id) then unit}
                                            {unit.symbol}
                                        {/await}
                                    </TableBodyCell>
                                    <TableBodyCell class="text-center"
                                        >{formatDate(
                                            testResult.test_date,
                                        )}</TableBodyCell
                                    >
                                    <TableBodyCell
                                        tdClass="flex justify-end gap-6"
                                    >
                                        <Button
                                            class="flex gap-2 text-gray-600 p-2"
                                            onclick={(e: any) => {
                                                e.preventDefault();
                                                e.stopPropagation();
                                                goto(
                                                    `/update-test-result/${testResult.id}`,
                                                );
                                            }}
                                        >
                                            Update
                                            <EditOutline class="h-6 w-6"
                                            ></EditOutline>
                                        </Button>
                                        <Button
                                            class="flex gap-2 p-2 text-gray-600"
                                            onclick={(e: any) => {
                                                e.preventDefault();
                                                e.stopPropagation();
                                                TestResultEntityInstance.delete(
                                                    Number(testResult.id),
                                                );
                                                testResults =
                                                    testResults.filter(
                                                        (t) =>
                                                            t.id !==
                                                            testResult.id,
                                                    );
                                            }}
                                        >
                                            Delete
                                            <TrashBinOutline class="h-6 w-6"
                                            ></TrashBinOutline>
                                        </Button>
                                    </TableBodyCell>
                                </TableBodyRow>
                            {/each}
                        </TableBody>
                    </Table>
                </TabItem>
            </Tabs>
        {/if}
    </Squeeze>
</Center>
