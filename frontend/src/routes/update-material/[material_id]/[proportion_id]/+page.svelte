<script lang="ts">
    import { page } from "$app/stores";
    import type { Material } from "$lib/entities/materials";
    import MaterialEntityInstance from "$lib/entities/materials";
    import type { Proportion } from "$lib/entities/proportions";
    import ProportionEntityInstance from "$lib/entities/proportions";
    import { onMount } from "svelte";
    import Center from "../../../../components/center.svelte";
    import Header from "../../../../components/header.svelte";
    import MaterialForm from "../../../../components/material-form.svelte";
    import Squeeze from "../../../../components/squeeze.svelte";

    let material: Material | null = null;
    let proportion: Proportion | null = null;
    onMount(() => {
        const sub = page.subscribe(async (value) => {
            const { material_id, proportion_id } = value.params;

            material = await MaterialEntityInstance.get(Number(material_id));
            proportion = await ProportionEntityInstance.get(
                Number(proportion_id),
            );
        });

        sub();
    });
</script>

<Center>
    <Header></Header>
    <Squeeze>
        <h1 class="mb-6 text-gray-600">Update Material</h1>
        {#if material && proportion}
            <MaterialForm
                materialForm={material}
                proportionForm={proportion}
                materialId={material.id}
                proportionId={proportion.id}
            ></MaterialForm>
        {/if}
    </Squeeze>
</Center>
