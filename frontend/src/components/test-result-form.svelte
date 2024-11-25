<script lang="ts">
    import { goto } from "$app/navigation";
    import { get } from "$lib/helpers";
    import { LocalStorage } from "$lib/localStorage";
    import TestResultEntityInstance, {
        type TestResultCreate,
    } from "$lib/entities/test-results";
    import { onMount } from "svelte";
    import { Button, Input, Label, Select } from "flowbite-svelte";
    import { getAllUnits } from "$lib/entities/units";

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

<div class="rounded-2xl p-6 bg-white shadow-xl">
    <div class="mb-6">
        <Label class="block mb-2" for="property_measured"
            >Property Measured</Label
        >
        <Input
            id="property_measured"
            type="text"
            size="lg"
            class="rounded-lg bg-slate-50 placeholder:text-slate-500 text-slate-500"
            placeholder="property measured"
            bind:value={form.property_measured}
        />
    </div>

    <div class="mb-6">
        <Label class="block mb-2" for="test_date">Test Date</Label>
        <Input
            type="date"
            placeholder="test date"
            size="lg"
            class="rounded-lg bg-slate-50 placeholder:text-slate-500 text-slate-500"
            bind:value={form.test_date}
        />
    </div>

    <div class="flex w-full gap-6">
        <div class="mb-6 w-full">
            <Label class="block mb-2" for="result">Result</Label>
            <Input
                id="result"
                type="number"
                size="lg"
                class="rounded-lg bg-slate-50 placeholder:text-slate-500 text-slate-500"
                placeholder="result"
                bind:value={form.result}
            />
        </div>

        {#await getAllUnits() then units}
            <div class="mb-6 w-full">
                <Label class="block mb-2" for="unit2">Unit</Label>
                <Select
                    id="unit2"
                    class="rounded-lg bg-slate-50 placeholder:text-slate-500 text-slate-500"
                    size="lg"
                    bind:value={form.unit_id}
                    items={units.map((u) => ({
                        value: u.id,
                        name: u.name,
                    }))}
                />
            </div>
        {/await}
    </div>

    <div class="flex w-full justify-end">
        <Button
            class="bg-primary p-3 px-5 flex shadow-xl"
            size="lg"
            onclick={submit}
        >
            {!testResultId ? "Create" : "Update"}
        </Button>
    </div>
</div>
