<script lang="ts">
    import { onMount } from "svelte";
    import Header from "../../components/header.svelte";
    import { goto } from "$app/navigation";
    import Center from "../../components/center.svelte";
    import Squeeze from "../../components/squeeze.svelte";
    import { Button, Input, Label } from "flowbite-svelte";
    import UserEntityInstance, { type User } from "$lib/entities/users";

    let user: User;
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

<Center>
    <Header></Header>
    <Squeeze>
        <div class="flex h-fit justify-center">
            <div class="rounded-2xl p-6 bg-white shadow-xl w-1/3">
                <div class="mb-6">
                    <Label for="username" class="block mb-2">Username</Label>
                    <Input
                        class="rounded-lg bg-slate-50 placeholder:text-slate-500"
                        size="lg"
                        id="username"
                        type="text"
                        placeholder="concrete_guy123"
                        bind:value={form.username}
                    />
                </div>
                <div class="mb-6 w-full">
                    <Label for="password" class="block mb-2">Password</Label>
                    <Input
                        class="rounded-lg bg-slate-50 placeholder:text-slate-500"
                        size="lg"
                        id="password"
                        type="password"
                        placeholder="password"
                        bind:value={form.password}
                    />
                </div>

                <div class="mb-6 w-full">
                    <Label for="first_name" class="block mb-2">First Name</Label
                    >
                    <Input
                        class="rounded-lg bg-slate-50 placeholder:text-slate-500"
                        size="lg"
                        id="first_name"
                        type="text"
                        placeholder="John"
                        bind:value={form.first_name}
                    />
                </div>

                <div class="mb-6 w-full">
                    <Label for="last_name" class="block mb-2">Last Name</Label>
                    <Input
                        class="rounded-lg bg-slate-50 placeholder:text-slate-500"
                        size="lg"
                        id="last_name"
                        type="text"
                        placeholder="Doe"
                        bind:value={form.last_name}
                    />
                </div>

                <div class="flex w-full justify-end">
                    <Button
                        class="bg-primary p-3 px-5 flex shadow-xl"
                        size="lg"
                        onclick={async () => {
                            UserEntityInstance.update(user.id, form);
                        }}
                    >
                        Update
                    </Button>
                </div>
            </div>
        </div>
    </Squeeze>
</Center>
