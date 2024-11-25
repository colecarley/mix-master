<script lang="ts">
    import SessionInstance from "$lib/session";
    import { Button, Input, Label } from "flowbite-svelte";
    import Center from "../../components/center.svelte";
    import Header from "../../components/header.svelte";
    import Squeeze from "../../components/squeeze.svelte";

    let username = "";
    let password = "";
</script>

<Center>
    <Header showLinks={false}></Header>
    <Squeeze>
        <div class="flex h-fit justify-center">
            <div class="rounded-2xl p-6 bg-white shadow-xl w-1/3">
                <h1 class="mb-6">Sign in</h1>
                <div class="mb-6">
                    <Label for="username" class="block mb-2">Username</Label>
                    <Input
                        class="rounded-lg bg-slate-50 placeholder:text-slate-500"
                        size="lg"
                        id="username"
                        type="text"
                        placeholder="concrete_guy123"
                        bind:value={username}
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
                        bind:value={password}
                    />
                </div>

                <div class="flex w-full justify-end">
                    <Button
                        class="bg-primary p-3 px-5 flex shadow-xl"
                        size="lg"
                        onclick={async () => {
                            await SessionInstance.login(username, password);
                        }}
                    >
                        Sign in
                    </Button>
                </div>
            </div>
        </div>
    </Squeeze>
</Center>
