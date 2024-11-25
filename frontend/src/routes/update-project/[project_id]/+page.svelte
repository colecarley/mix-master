<script lang="ts">
    import { page } from "$app/stores";
    import type { Project } from "$lib/entities/projects";
    import ProjectEntityInstance from "$lib/entities/projects";
    import { onMount } from "svelte";
    import Center from "../../../components/center.svelte";
    import Header from "../../../components/header.svelte";
    import ProjectForm from "../../../components/project-form.svelte";
    import Squeeze from "../../../components/squeeze.svelte";

    let project: Project | null = $state(null);
    onMount(() => {
        const sub = page.subscribe(async (value) => {
            const { project_id } = value.params;

            project = await ProjectEntityInstance.get(Number(project_id));
        });

        sub();
    });
</script>

<Header></Header>
<Center>
    <Squeeze>
        <h1 class="mb-6">Update Project</h1>
        {#if project}
            <ProjectForm form={project} projectId={project.id}></ProjectForm>
        {/if}
    </Squeeze>
</Center>
