<script lang="ts">
    import { onDestroy, onMount } from "svelte";
    import MaterialForm from "../../../../components/material-form.svelte";
    import { page } from "$app/stores";
    import type { Material } from "$lib/entities/materials";
    import type { Proportion } from "$lib/entities/proportions";
    import ProportionEntityInstance from "$lib/entities/proportions";
    import MaterialEntityInstance from "$lib/entities/materials";
    import Center from "../../../../components/center.svelte";
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
    <Squeeze>
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
