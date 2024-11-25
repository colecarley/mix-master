<script lang="ts">
    import Header from "../../../components/header.svelte";

    import { goto } from "$app/navigation";
    import { page } from "$app/stores";
    import MaterialEntityInstance from "$lib/entities/materials";
    import MixEntityInstance, { type Mix } from "$lib/entities/mixes";
    import ProjectEntityInstance, {
        type Project,
    } from "$lib/entities/projects";
    import TestResultEntityInstance from "$lib/entities/test-results";
    import { formatDate } from "$lib/helpers";
    import { LocalStorage } from "$lib/localStorage";
    import { Button, Listgroup, TabItem, Tabs } from "flowbite-svelte";
    import {
        EditOutline,
        PlusOutline,
        TrashBinOutline,
    } from "flowbite-svelte-icons";
    import { onMount } from "svelte";
    import Center from "../../../components/center.svelte";
    import MmCard from "../../../components/mm-card.svelte";
    import Squeeze from "../../../components/squeeze.svelte";

    let userId: string;
    let projectId: string;
    let project: Project;
    let mixes: Mix[];

    type Stat = {
        name: string;
        value: string;
    };

    let stats: Stat[] = [];

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

            let totalMaterials = 0;
            let totalTestResults = 0;
            for (const mix of mixes) {
                const materials = await MaterialEntityInstance.getAll();
                totalMaterials += materials.length;

                const testResults = await TestResultEntityInstance.getAll();
                totalTestResults += testResults.length;
            }

            stats = [
                {
                    name: "Total Mixes",
                    value: mixes.length.toString(),
                },
                {
                    name: "Total Materials",
                    value: totalMaterials.toString(),
                },
                {
                    name: "Total Test Results",
                    value: totalTestResults.toString(),
                },
            ];
        });

        sub();
    });
</script>

<Header></Header>
<Center>
    <Squeeze>
        <Tabs>
            <TabItem
                title="Project"
                open
                activeClasses="p-4 text-white rounded-xl bg-primary shadow-xl text-lg"
                inactiveClasses="p-4 rounded-xl text-lg bg-white text-primary"
            >
                <h1>Project</h1>
                <div class="mb-6">
                    {#if project}
                        <MmCard
                            title={project.name}
                            subtitle={formatDate(project.created_at)}
                            description={project.description}
                            onUpdate={() => {
                                goto(`/update-project/${project.id}`);
                            }}
                        ></MmCard>
                    {/if}
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
                    {#each stats as stat}
                        <MmCard title={stat.name} description={stat.value}
                        ></MmCard>
                    {/each}
                </div>
                <div class="flex justify-end">
                    <Button
                        class="bg-primary flex gap-2"
                        onclick={() => {
                            ProjectEntityInstance.delete(Number(projectId));
                            goto("/projects");
                        }}
                    >
                        <TrashBinOutline class="h-4 w-4"></TrashBinOutline>
                        Delete
                    </Button>
                </div>
            </TabItem>
            <TabItem
                title="Mixes"
                activeClasses="p-4 text-white rounded-xl bg-primary shadow-xl text-lg"
                inactiveClasses="p-4 rounded-xl text-lg bg-white text-primary"
            >
                <div class="flex justify-between">
                    <h1>Mixes</h1>
                    <button
                        onclick={() => {
                            goto("/create-mix");
                        }}
                    >
                        <PlusOutline class="h-10 w-10"></PlusOutline>
                    </button>
                </div>

                <Listgroup items={mixes} let:item class="shadow-xl" active>
                    <a
                        href="/projects/{projectId}/mixes/{item.id}"
                        class="flex justify-between w-full"
                    >
                        <div class="mb-2 flex flex-col">
                            <div class="mb-2 text-start">
                                <h2 class="mb-2">{item.name}</h2>
                                <p>{formatDate(item.created_at)}</p>
                            </div>
                            <p class="text-start">{item.description}</p>
                        </div>
                    </a>
                </Listgroup>
            </TabItem>
        </Tabs>
    </Squeeze>
</Center>
