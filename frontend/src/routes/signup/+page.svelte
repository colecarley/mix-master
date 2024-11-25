<script>
    import { goto } from "$app/navigation";
    import { post } from "$lib/helpers";
    import { LocalStorage } from "$lib/localStorage";
    import Center from "../../components/center.svelte";
    import Squeeze from "../../components/squeeze.svelte";

    let form = {
        username: "",
        password: "",
        first_name: "",
        last_name: "",
    };
</script>

<Center>
    <Squeeze>
        <input type="text" placeholder="username" bind:value={form.username} />
        <input
            type="password"
            placeholder="password"
            bind:value={form.password}
        />
        <input
            type="text"
            placeholder="first name"
            bind:value={form.first_name}
        />
        <input
            type="text"
            placeholder="last name"
            bind:value={form.last_name}
        />

        <button
            type="submit"
            onclick={async () => {
                const response = await post("/signup/", form);

                if (!response.ok) {
                    console.error("error");
                    return;
                }

                const user = await response.json();

                LocalStorage.CurrentUserId.set(user.id);

                goto("/projects");
            }}>sign up</button
        >
    </Squeeze>
</Center>
