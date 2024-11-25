<script lang="ts">
    import { Button, Card } from "flowbite-svelte";
    import { EditOutline, TrashBinOutline } from "flowbite-svelte-icons";
    export let title: string;
    export let description: string;
    export let href: string;
    export let onUpdate: (e: any) => void;
    export let onDelete: (e: any) => void;
</script>

<Card {href} class="rounded-lg p-5 shadow-xl">
    <div class="flex justify-between">
        <h2>{title}</h2>
        <Button onclick={onUpdate}>
            <EditOutline class="h-6 w-6"></EditOutline>
        </Button>
    </div>

    <p>{description}</p>
    <div class="flex w-full">
        <Button onclick={onDelete}>
            <TrashBinOutline class="h-6 w-6"></TrashBinOutline>
        </Button>
    </div>
</Card>
