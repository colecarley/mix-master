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
            <button onclick={() => goto("/create-material")}
                >Add Material</button
            >
        </div>
        <div class="flex flex-col">
            {#each materialsWithProportions as material}
                <div class="border border-black">
                    <h2>{material.name}</h2>
                    <p>{material.proportion?.quantity}</p>
                    <button
                        onclick={(e) => {
                            e.preventDefault();
                            e.stopPropagation();
                            ProportionEntityInstance.delete(
                                Number(material.proportion.id),
                            );
                            MaterialEntityInstance.delete(Number(material.id));

                            materialsWithProportions =
                                materialsWithProportions.filter(
                                    (m) => m.id !== material.id,
                                );
                        }}>Delete</button
                    >
                    <button
                        onclick={(e) => {
                            e.preventDefault();
                            e.stopPropagation();
                            goto(
                                `/update-material/${material.id}/${material.proportion.id}`,
                            );
                        }}>Update</button
                    >
                </div>
            {/each}
        </div>
        <div class="w-full flex justify-between">
            <h1>Test Result</h1>
            <button onclick={() => goto("/create-test-result")}
                >Add Test Result</button
            >
        </div>
        <div class="flex flex-col">
            {#each testResults as testResult}
                <div class="border border-black">
                    <h2>{testResult.property_measured}</h2>
                    <p>{testResult.result}</p>
                    <button
                        onclick={(e) => {
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
                    </button>
                    <button
                        onclick={(e) => {
                            e.preventDefault();
                            e.stopPropagation();
                            goto(`/update-test-result/${testResult.id}`);
                        }}>Update</button
                    >
                </div>
            {/each}
        </div></Squeeze
    >
</Center>
