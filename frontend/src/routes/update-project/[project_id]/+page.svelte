<script lang="ts">
    import { page } from "$app/stores";
    import { onMount } from "svelte";
    import ProjectForm from "../../../components/project-form.svelte";
    import type { Project } from "$lib/entities/projects";
    import ProjectEntityInstance from "$lib/entities/projects";
    import Squeeze from "../../../components/squeeze.svelte";
    import Center from "../../../components/center.svelte";

    let project: Project | null = $state(null);
    onMount(() => {
        const sub = page.subscribe(async (value) => {
            const { project_id } = value.params;

            project = await ProjectEntityInstance.get(Number(project_id));
        });

        sub();
    });
</script>

<Center>
    <Squeeze>
        {#if project}
            <ProjectForm form={project} projectId={project.id}></ProjectForm>
        {/if}
    </Squeeze>
</Center>
