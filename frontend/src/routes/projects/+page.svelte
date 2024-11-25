<script lang="ts">
    import { goto } from "$app/navigation";
    import { onMount } from "svelte";
    import ProjectEntityInstance, {
        ProjectEntity,
        type Project,
    } from "$lib/entities/projects";
    import Header from "../../components/header.svelte";
    import Center from "../../components/center.svelte";
    import Squeeze from "../../components/squeeze.svelte";
    import { LocalStorage } from "$lib/localStorage";
    import { Card, Button } from "flowbite-svelte";
    import {
        CirclePlusOutline,
        EditOutline,
        PlusOutline,
        TrashBinOutline,
    } from "flowbite-svelte-icons";
    import MmCard from "../../components/mm-card.svelte";

    let projects: Project[] = [];
    onMount(async () => {
        const userId = LocalStorage.CurrentUserId.get();
        if (!userId) {
            goto("/signin");
            return;
        }

        const projectEntity = new ProjectEntity();
        projects = await projectEntity.getAll();

        if (!projects.length) {
            console.error("error");
            return;
        }
    });

    function createNewProject() {
        goto("/create-project");
    }

    function deleteProject(project: Project) {
        ProjectEntityInstance.delete(Number(project.id));
        projects = projects.filter((p) => p.id !== project.id);
    }
</script>

<Header></Header>

<Center>
    <Squeeze>
        <div class="w-full flex justify-between">
            <h1>Projects</h1>
            <button onclick={() => createNewProject()}>
                <PlusOutline class="h-6 w-6"></PlusOutline>
            </button>
        </div>
        <div class="flex gap-4">
            {#each projects as project}
                <MmCard
                    title={project.name}
                    description={project.description}
                    href="/projects/{project.id}"
                    onDelete={(e) => {
                        e.preventDefault();
                        e.stopPropagation();
                        deleteProject(project);
                    }}
                    onUpdate={(e) => {
                        e.preventDefault();
                        e.stopPropagation();
                        goto(`/update-project/${project.id}`);
                    }}
                ></MmCard>
            {/each}
        </div>
    </Squeeze>
</Center>
