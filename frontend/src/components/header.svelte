<script lang="ts">
    import { goto } from "$app/navigation";
    import SessionInstance from "$lib/session";

    let { showLinks = true } = $props();
</script>

<header class="w-full flex p-8 bg-primary items-center text-white mb-12">
    <a href="/">
        <h1>MixMaster</h1>
    </a>
    {#if showLinks}
        <div class="w-full flex justify-end">
            <nav class="flex justify-between w-1/6">
                <button
                    class="hover:underline"
                    onclick={() => goto("/projects")}>Projects</button
                >
                <button class="hover:underline" onclick={() => goto("/profile")}
                    >Profile</button
                >
                <button
                    class="hover:underline"
                    onclick={() => {
                        SessionInstance.logout();
                    }}>Log out</button
                >
            </nav>
        </div>
    {/if}
</header>
