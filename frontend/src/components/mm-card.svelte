<script lang="ts">
    import { Button, Card } from "flowbite-svelte";
    import { EditOutline, TrashBinOutline } from "flowbite-svelte-icons";
    export let title: string;
    export let subtitle: string | null = null;
    export let description: string;
    export let href: string | null = null;
    export let onUpdate: ((e: any) => void) | null = null;
    export let onDelete: ((e: any) => void) | null = null;
</script>

<Card href={href ? href : ""} class="rounded-xl p-5 shadow-xl bg-white">
    <div class="flex justify-between">
        <h2>{title}</h2>

        {#if onUpdate}
            <Button onclick={onUpdate}>
                <EditOutline class="h-6 w-6 text-gray-600"></EditOutline>
            </Button>
        {/if}
    </div>
    {#if subtitle}
        <p>{subtitle}</p>
    {/if}

    <p>{description}</p>
    {#if onDelete}
        <div class="flex w-full justify-end">
            <Button
                onclick={onDelete}
                class="bg-orange-600 text-slate-100 p-2 px-4"
            >
                <div class="flex gap-2 justify-end">
                    <span class="font-bold">Delete </span>
                    <TrashBinOutline class="h-6 w-6"></TrashBinOutline>
                </div>
            </Button>
        </div>
    {/if}

    <slot></slot>
</Card>
