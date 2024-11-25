<script lang="ts">
    import { page } from "$app/stores";
    import MixEntityInstance, { type Mix } from "$lib/entities/mixes";
    import { onMount } from "svelte";
    import Center from "../../../components/center.svelte";
    import Header from "../../../components/header.svelte";
    import MixForm from "../../../components/mix-form.svelte";
    import Squeeze from "../../../components/squeeze.svelte";

    let mix: Mix | null = $state(null);
    onMount(() => {
        const sub = page.subscribe(async (value) => {
            const { mix_id } = value.params;

            mix = await MixEntityInstance.get(Number(mix_id));
        });

        sub();
    });
</script>

<Header></Header>
<Center>
    <Squeeze>
        <h1 class="mb-6">Update Mix</h1>
        {#if mix}
            <MixForm form={mix} mixId={mix.id}></MixForm>
        {/if}
    </Squeeze>
</Center>
