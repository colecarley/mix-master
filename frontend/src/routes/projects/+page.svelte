<script lang="ts">
    import { goto } from "$app/navigation";
    import ProjectEntityInstance, {
        ProjectEntity,
        type Project,
    } from "$lib/entities/projects";
    import { LocalStorage } from "$lib/localStorage";
    import { PlusOutline } from "flowbite-svelte-icons";
    import { onMount } from "svelte";
    import Center from "../../components/center.svelte";
    import Header from "../../components/header.svelte";
    import MmCard from "../../components/mm-card.svelte";
    import Squeeze from "../../components/squeeze.svelte";

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

<Center>
    <Header></Header>
    <Squeeze>
        <div class="w-full flex justify-between">
            <h1 class="text-gray-600">Projects</h1>
            <button onclick={() => createNewProject()}>
                <PlusOutline class="h-10 w-10 text-gray-600"></PlusOutline>
            </button>
        </div>
        <div class="grid grid-cols-2 gap-6">
            {#each projects as project}
                <MmCard
                    title={project.name}
                    description={project.description}
                    href="/projects/{project.id}"
                ></MmCard>
            {/each}
        </div>
    </Squeeze>
</Center>
