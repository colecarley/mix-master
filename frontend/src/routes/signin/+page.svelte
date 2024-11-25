<script lang="ts">
    import { goto } from "$app/navigation";
    import { post } from "$lib/helpers";
    import { LocalStorage } from "$lib/localStorage";
    import Center from "../../components/center.svelte";
    import Squeeze from "../../components/squeeze.svelte";

    let username = "";
    let password = "";
</script>

<Center>
    <Squeeze>
        <input type="text" placeholder="username" bind:value={username} />
        <input type="password" placeholder="password" bind:value={password} />
        <button
            type="submit"
            onclick={async () => {
                const response = await post("/login/", {
                    username,
                    password,
                });

                if (response.ok) {
                    const { id } = await response.json();

                    LocalStorage.CurrentUserId.set(id);
                    goto("/projects");
                } else {
                    console.error("error");
                }
            }}>sign in</button
        >
    </Squeeze>
</Center>
