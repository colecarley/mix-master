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

<Header></Header>

<Center>
    <Squeeze>
        <h1>Create Material</h1>
        <input
            type="text"
            placeholder="material name"
            bind:value={materialForm.name}
        />
        <input
            type="number"
            placeholder="cost per unit"
            bind:value={materialForm.cost_per_unit}
        />
        <select placeholder="unit" bind:value={materialForm.unit_id}>
            {#await getAllUnits() then units}
                {#each units as unit}
                    <option value={unit.id}>{unit.name}</option>
                {/each}
            {/await}
        </select>

        <input
            type="number"
            placeholder="quantity"
            bind:value={proportionForm.quantity}
        />
        <select placeholder="unit" bind:value={proportionForm.unit_id}>
            {#await getAllUnits() then units}
                {#each units as unit}
                    <option value={unit.id}>{unit.name}</option>
                {/each}
            {/await}
        </select>
        <button onclick={submit}
            >{!materialId || !proportionId ? "Create" : "Update"}</button
        >
    </Squeeze>
</Center>
