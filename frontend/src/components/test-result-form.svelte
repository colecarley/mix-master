<script lang="ts">
    import { goto } from "$app/navigation";
    import { get } from "$lib/helpers";
    import { LocalStorage } from "$lib/localStorage";
    import TestResultEntityInstance, {
        type TestResultCreate,
    } from "$lib/entities/test-results";
    import { onMount } from "svelte";

    export let form: TestResultCreate = {
        test_date: "",
        property_measured: "",
        result: null as unknown as number,
        unit_id: null as unknown as number,
        mix_id: null as unknown as number,
    };

    export let testResultId: number | null;

    onMount(() => {
        const temp = LocalStorage.CurrentMixId.get();
        if (!temp) {
            return;
        }

        form.mix_id = Number(temp);
    });

    function submit() {
        if (!testResultId) {
            create();
        } else {
            update();
        }
    }

    async function create() {
        await TestResultEntityInstance.create(form);
        const projectId = LocalStorage.CurrentProjectId.get();
        goto(`/projects/${projectId}/mixes/${form.mix_id}`);
    }

    async function update() {
        if (!testResultId) {
            return;
        }
        console.log("updating");
        const result = await TestResultEntityInstance.update(
            testResultId,
            form,
        );
        console.log(result);

        const projectId = LocalStorage.CurrentProjectId.get();
        goto(`/projects/${projectId}/mixes/${form.mix_id}`);
    }

    async function getUnits() {
        const response = await get("/units");
        return await response.json();
    }
</script>

<input
    type="text"
    placeholder="property measured"
    bind:value={form.property_measured}
/>
<input type="date" placeholder="test date" bind:value={form.test_date} />
<input type="number" placeholder="result" bind:value={form.result} />

<select placeholder="unit" bind:value={form.unit_id}>
    {#await getUnits() then units}
        {#each units as unit}
            <option value={unit.id}>{unit.name}</option>
        {/each}
    {/await}
</select>

<button onclick={submit}>{!testResultId ? "Create" : "Update"}</button>
