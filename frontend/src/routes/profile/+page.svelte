<script lang="ts">
    import { onMount } from "svelte";
    import Header from "../../components/header.svelte";
    import { goto } from "$app/navigation";
    import Center from "../../components/center.svelte";
    import Squeeze from "../../components/squeeze.svelte";

    let user;
    let form = {
        username: "",
        first_name: "",
        last_name: "",
        password: "",
    };

    onMount(async () => {
        const userId = localStorage.getItem("mixMasterCurrentUserId");
        if (!userId) {
            goto("/signin");
            return;
        }

        const response = await fetch(`http://127.0.0.1:8000/users/${userId}`);

        if (!response.ok) {
            console.error("error");
            return;
        }

        user = await response.json();

        form = {
            username: user.username,
            first_name: user.first_name,
            last_name: user.last_name,
            password: user.password,
        };

        console.log(user);
    });
</script>

<Header></Header>
<Center>
    <Squeeze>
        <input
            type="text"
            placeholder="First Name"
            bind:value={form.first_name}
        />
        <input
            type="text"
            placeholder="Last Name"
            bind:value={form.last_name}
        />
        <input type="text" placeholder="username" bind:value={form.username} />
        <input type="text" placeholder="passowrd" bind:value={form.password} />
    </Squeeze>
</Center>
