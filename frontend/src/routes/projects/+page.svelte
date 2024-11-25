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
            <button onclick={() => createNewProject()}>New Project</button>
        </div>
        <div class="flex flex-col gap-4">
            {#each projects as project}
                <a href="/projects/{project.id}">
                    <div class="border border-black">
                        <h2>{project.name}</h2>
                        <p>{project.description}</p>
                        <button
                            onclick={(e) => {
                                e.preventDefault();
                                e.stopPropagation();
                                deleteProject(project);
                            }}>Delete</button
                        >

                        <button
                            onclick={(e) => {
                                e.preventDefault();
                                e.stopPropagation();
                                goto(`/update-project/${project.id}`);
                            }}>Update</button
                        >
                    </div>
                </a>
            {/each}
        </div>
    </Squeeze>
</Center>
