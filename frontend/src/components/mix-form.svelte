<script lang="ts">
    import { goto } from "$app/navigation";
    import { onMount } from "svelte";
    import { LocalStorage } from "$lib/localStorage";
    import MixEntityInstance, { type MixCreate } from "$lib/entities/mixes";
    import Center from "./center.svelte";
    import Squeeze from "./squeeze.svelte";
    import { Button, Input, Label, Textarea } from "flowbite-svelte";

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

<div class="rounded-2xl p-6 bg-white shadow-xl">
    <div class="mb-6">
        <Label for="mix" class="block mb-2">Mix Name</Label>
        <Input
            class="rounded-lg bg-slate-50 placeholder:text-slate-500"
            size="lg"
            id="mix"
            type="text"
            placeholder="mix one"
            bind:value={form.name}
        />
    </div>

    <div class="mb-6">
        <Label for="description" class="block mb-2">Description</Label>
        <Textarea
            id="description"
            class="rounded-lg bg-slate-50 description"
            rows={4}
            bind:value={form.description}
        />
    </div>
    <div class="flex w-full justify-end">
        <Button class="bg-orange-600 p-3 px-5 flex shadow-xl" onclick={submit}
            >{mixId ? "Update" : "Create"}</Button
        >
    </div>
</div>
