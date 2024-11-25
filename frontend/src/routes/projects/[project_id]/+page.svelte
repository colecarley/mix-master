<script lang="ts">
    import Header from "../../../components/header.svelte";

    import { page } from "$app/stores";
    import { onMount } from "svelte";
    import Squeeze from "../../../components/squeeze.svelte";
    import Center from "../../../components/center.svelte";
    import { goto } from "$app/navigation";
    import { formatDate, get } from "$lib/helpers";
    import { LocalStorage } from "$lib/localStorage";
    import ProjectEntityInstance, {
        type Project,
    } from "$lib/entities/projects";
    import MixEntityInstance, { type Mix } from "$lib/entities/mixes";

    let userId: string;
    let projectId: string;
    let project: Project;
    let mixes: Mix[];

    onMount(async () => {
        const sub = page.subscribe(async (value) => {
            projectId = value.params.project_id;
            LocalStorage.CurrentProjectId.set(projectId);

            const temp = LocalStorage.CurrentUserId.get();
            if (!temp) {
                return;
            }

            userId = temp;

            project = await ProjectEntityInstance.get(Number(projectId));
            mixes = await MixEntityInstance.getAll();
        });

        sub();
    });
</script>

<Header></Header>
<Center>
    <Squeeze>
        <h1>Project</h1>

        {#if project}
            <h2>{project.name}</h2>
            <p>{formatDate(project.created_at)}</p>
            <p>{project.description}</p>
        {/if}
        <div class="flex justify-between">
            <h1>Mixes</h1>
            <button
                onclick={() => {
                    goto("/create-mix");
                }}>New Mix</button
            >
        </div>
        <div class="flex flex-col">
            {#each mixes as mix}
                <a href="/projects/{projectId}/mixes/{mix.id}">
                    <h2>{mix.name}</h2>
                    <p>{formatDate(mix.created_at)}</p>
                    <p>{mix.description}</p>
                    <button
                        onclick={(e) => {
                            e.preventDefault();
                            e.stopPropagation();
                            MixEntityInstance.delete(Number(mix.id));
                            mixes = mixes.filter((m) => m.id !== mix.id);
                        }}>Delete</button
                    >
                    <button
                        onclick={(e) => {
                            e.preventDefault();
                            e.stopPropagation();
                            goto(`/update-mix/${mix.id}`);
                        }}
                    >
                        Update
                    </button>
                </a>
            {/each}
        </div>
    </Squeeze>
</Center>
