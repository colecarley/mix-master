<script lang="ts">
    import { goto } from "$app/navigation";
    import SessionInstance from "$lib/session";

    let { showLinks = true } = $props();
</script>

<header class="w-full flex p-10 bg-orange-600 items-center text-white mb-12">
    <h1>MixMaster</h1>
    {#if showLinks}
        <div class="w-full flex justify-end">
            <nav class="flex justify-between w-1/6">
                <button onclick={() => goto("/projects")}>Projects</button>
                <button onclick={() => goto("/profile")}>Profile</button>
                <button
                    onclick={() => {
                        SessionInstance.logout();
                    }}>Log out</button
                >
            </nav>
        </div>
    {/if}
</header>
