<script>
    import { goto } from "$app/navigation";
    import { post } from "$lib/helpers";
    import { LocalStorage } from "$lib/localStorage";
    import { Button, Input, Label } from "flowbite-svelte";
    import Center from "../../components/center.svelte";
    import Header from "../../components/header.svelte";
    import Squeeze from "../../components/squeeze.svelte";

    let form = {
        username: "",
        password: "",
        first_name: "",
        last_name: "",
    };
</script>

<Center>
    <Header showLinks={false}></Header>
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
                        class="bg-orange-600 p-3 px-5 flex shadow-xl"
                        size="lg"
                        onclick={async () => {
                            const response = await post("/signup/", form);

                            if (!response.ok) {
                                console.error("error");
                                return;
                            }

                            const user = await response.json();

                            LocalStorage.CurrentUserId.set(user.id);

                            goto("/projects");
                        }}
                    >
                        Sign Up!
                    </Button>
                </div>
            </div>
        </div>
    </Squeeze>
</Center>
