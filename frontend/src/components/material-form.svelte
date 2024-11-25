<script lang="ts">
    import { goto } from "$app/navigation";
    import { get, post } from "$lib/helpers";
    import { LocalStorage } from "$lib/localStorage";
    import type { MaterialCreate } from "$lib/entities/materials";
    import type { ProportionCreate } from "$lib/entities/proportions";
    import { getAllUnits } from "$lib/entities/units";
    import Header from "./header.svelte";
    import Center from "./center.svelte";
    import Squeeze from "./squeeze.svelte";
    import ProportionEntityInstance from "$lib/entities/proportions";
    import MaterialEntityInstance from "$lib/entities/materials";
    import { Button, Input, Label, Select } from "flowbite-svelte";

    export let materialForm: MaterialCreate = {
        mix_id: null as unknown as number,
        name: "",
        cost_per_unit: null as unknown as number,
        unit_id: null as unknown as number,
    };

    export let proportionForm: ProportionCreate = {
        mix_id: null as unknown as number,
        material_id: null as unknown as number,
        quantity: null as unknown as number,
        unit_id: null as unknown as number,
    };

    export let materialId: number | null;
    export let proportionId: number | null;

    async function submit() {
        if (!materialId || !proportionId) {
            create();
        } else {
            update();
        }
    }

    async function create() {
        const mixId = Number(LocalStorage.CurrentMixId.get());

        materialForm.mix_id = mixId;
        proportionForm.mix_id = mixId;

        const { id } = await MaterialEntityInstance.create(materialForm);

        proportionForm.material_id = id;
        ProportionEntityInstance.create(proportionForm);

        const projectId = Number(LocalStorage.CurrentProjectId.get());
        goto(`/projects/${projectId}/mixes/${mixId}`);
    }

    async function update() {
        const mixId = Number(LocalStorage.CurrentMixId.get());

        materialForm.mix_id = mixId;
        proportionForm.mix_id = mixId;

        if (!materialId || !proportionId) {
            return;
        }
        await MaterialEntityInstance.update(materialId, materialForm);

        proportionForm.material_id = materialId;
        console.log(proportionForm);
        ProportionEntityInstance.update(proportionId, proportionForm);

        const projectId = Number(LocalStorage.CurrentProjectId.get());
        goto(`/projects/${projectId}/mixes/${mixId}`);
    }
</script>

<Center>
    <Squeeze>
        <h1>Create Material</h1>
        <div class="rounded-2xl p-6 bg-white shadow-xl">
            <div class="mb-6">
                <Label for="material" class="block mb-2">Material Name</Label>
                <Input
                    class="rounded-lg bg-slate-50 placeholder:text-slate-500"
                    size="lg"
                    id="material"
                    type="text"
                    placeholder="cement"
                    bind:value={materialForm.name}
                />
            </div>
            <div class="flex w-full gap-6">
                <div class="mb-6 w-full">
                    <Label for="cost_per_unit" class="block mb-2"
                        >Cost Per Unit</Label
                    >
                    <Input
                        class="rounded-lg bg-slate-50 placeholder:text-slate-500"
                        size="lg"
                        id="cost_per_unit"
                        type="number"
                        placeholder="20"
                        bind:value={materialForm.cost_per_unit}
                    />
                </div>
                {#await getAllUnits() then units}
                    <div class="mb-6 w-full">
                        <Label class="block mb-2" for="unit">Unit</Label>
                        <Select
                            id="unit"
                            class="rounded-lg bg-slate-50 placeholder:text-slate-500 p-4 text-slate-500"
                            bind:value={materialForm.unit_id}
                            items={units.map((u) => ({
                                value: u.id,
                                name: u.name,
                            }))}
                        />
                    </div>
                {/await}
            </div>

            <div class="flex w-full gap-6">
                <div class="mb-6 w-full">
                    <Label for="quantity" class="block mb-2">Quantity</Label>
                    <Input
                        id="quantity"
                        class="rounded-lg bg-slate-50 placeholder:text-slate-500"
                        size="lg"
                        type="number"
                        placeholder="quantity"
                        bind:value={proportionForm.quantity}
                    />
                </div>

                {#await getAllUnits() then units}
                    <div class="mb-6 w-full">
                        <Label class="block mb-2" for="unit2">Unit</Label>
                        <Select
                            id="unit2"
                            class="rounded-lg bg-slate-50 placeholder:text-slate-500 p-4 text-slate-500"
                            bind:value={proportionForm.unit_id}
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
                    class="bg-orange-600 p-3 px-5 flex shadow-xl"
                    size="lg"
                    onclick={submit}
                    >{!materialId || !proportionId
                        ? "Create"
                        : "Update"}</Button
                >
            </div>
        </div>
    </Squeeze>
</Center>
