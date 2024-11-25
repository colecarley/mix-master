<script lang="ts">
    import { goto } from "$app/navigation";
    import { onMount } from "svelte";
    import { LocalStorage } from "$lib/localStorage";
    import MixEntityInstance, { type MixCreate } from "$lib/entities/mixes";
    import Center from "./center.svelte";
    import Squeeze from "./squeeze.svelte";

    export let form: MixCreate = {
        name: "",
        description: "",
        project_id: null as unknown as number,
    };

    export let mixId: number | null;

    let currentProjectId;
    onMount(() => {
        currentProjectId = LocalStorage.CurrentProjectId.get();
        if (!currentProjectId) {
            return;
        }

        form.project_id = Number(currentProjectId);
    });

    function submit() {
        if (!mixId) {
            create();
        } else {
            update();
        }
    }

    async function create() {
        await MixEntityInstance.create(form);
        goto(`/projects/${LocalStorage.CurrentProjectId.get()}`);
    }

    async function update() {
        if (!mixId) {
            return;
        }
        console.log("updating");
        const result = await MixEntityInstance.update(mixId, form);
        console.log(result);

        goto(`/projects/${LocalStorage.CurrentProjectId.get()}`);
    }
</script>

<Center>
    <Squeeze>
        <input type="text" placeholder="mix name" bind:value={form.name} />
        <input
            type="text"
            placeholder="description"
            bind:value={form.description}
        />
        <button onclick={submit}>{mixId ? "Update" : "Create"}</button>
    </Squeeze>
</Center>
