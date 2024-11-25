<script lang="ts">
    let { showLinks = true } = $props();
</script>

<header class="w-full flex p-10 bg-orange-600 items-center text-white mb-12">
    <h1>MixMaster</h1>
    {#if showLinks}
        <div class="w-full flex justify-end">
            <nav class="flex justify-between w-1/3">
                <a href="/projects">Projects</a>
                <a href="/profile">Profile</a>
                <a href="/">Log out</a>
            </nav>
        </div>
    {/if}
</header>
