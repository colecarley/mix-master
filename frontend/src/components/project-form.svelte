<script lang="ts">
    import { goto } from "$app/navigation";
    import ProjectEntityInstance, {
        type ProjectCreate,
    } from "$lib/entities/projects";
    import { LocalStorage } from "$lib/localStorage";
    import { Button, Input, Label } from "flowbite-svelte";
    import { onMount } from "svelte";

    export let form: ProjectCreate = {
        name: "",
        description: "",
        user_id: null as unknown as number,
        start_date: null as unknown as string,
        end_date: null as unknown as string,
    };

    export let projectId: number | null = null;

    onMount(() => {
        const temp = LocalStorage.CurrentUserId.get();
        if (!temp) {
            return;
        }

        form.user_id = Number(temp);
    });

    function submit() {
        if (!projectId) {
            create();
        } else {
            update();
        }
    }

    async function create() {
        const { id } = await ProjectEntityInstance.create(form);
        goto(`/projects/${id}`);
    }

    async function update() {
        if (!projectId) {
            return;
        }

        await ProjectEntityInstance.update(projectId, form);
        goto(`/projects/${projectId}`);
    }
</script>

<div class="rounded-2xl p-6 bg-white shadow-xl">
    <div class="mb-6">
        <Label for="project" class="block mb-2">Project Name</Label>
        <Input
            id="project"
            size="lg"
            class="rounded-lg bg-slate-50 placeholder:text-slate-500 p-4 text-slate-500"
            type="text"
            placeholder="project one"
            bind:value={form.name}
        />
    </div>

    <div class="mb-6">
        <Label for="description" class="block mb-2">Description</Label>
        <Input
            id="description"
            class="rounded-lg bg-slate-50 placeholder:text-slate-500 p-4 text-slate-500"
            size="lg"
            type="text"
            placeholder="description"
            bind:value={form.description}
        />
    </div>

    <div class="flex gap-6">
        <div class="mb-6 w-full">
            <Label for="start_date" class="block mb-2">Start Date</Label>
            <Input
                id="start_date"
                class="rounded-lg bg-slate-50 placeholder:text-slate-500 p-4 text-slate-500"
                size="lg"
                type="date"
                placeholder="start date"
                bind:value={form.start_date}
            />
        </div>

        <div class="mb-6 w-full">
            <Label for="end_date" class="block mb-2">End Date</Label>
            <Input
                id="end_date"
                class="rounded-lg bg-slate-50 placeholder:text-slate-500 p-4 text-slate-500"
                size="lg"
                type="date"
                placeholder="end date"
                bind:value={form.end_date}
            />
        </div>
    </div>
    <div class="flex w-fulll justify-end">
        <Button class="bg-orange-600 p-3 px-5 flex shadow-xl" onclick={submit}
            >{projectId ? "Update" : "Create"}</Button
        >
    </div>
</div>
