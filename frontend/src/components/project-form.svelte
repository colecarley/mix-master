<script lang="ts">
    import { goto } from "$app/navigation";
    import ProjectEntityInstance, {
        type ProjectCreate,
    } from "$lib/entities/projects";
    import { LocalStorage } from "$lib/localStorage";
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

<input type="text" placeholder="project name" bind:value={form.name} />
<input type="text" placeholder="description" bind:value={form.description} />
<input type="date" placeholder="start date" bind:value={form.start_date} />
<input type="date" placeholder="end date" bind:value={form.end_date} />
<button onclick={submit}>{projectId ? "Update" : "Create"}</button>
