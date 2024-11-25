<script>
    import { goto } from "$app/navigation";
    import { Button } from "flowbite-svelte";
    import Center from "../components/center.svelte";
    import Header from "../components/header.svelte";
    import MmCard from "../components/mm-card.svelte";
    import Squeeze from "../components/squeeze.svelte";
</script>

<Header showLinks={false}></Header>

<Center>
    <Squeeze>
        <h1 class="text-4xl font-light mb-6 text-gray-600">
            WELOME TO MIXMASTER
        </h1>
        <p
            class="text-8xl mb-6 text-gray-600
            "
        >
            The best platform for keeping track of your concrete mix designs...
        </p>

        <div class="mb-6">
            <h2 class="text-3xl font-light mb-6 text-gray-600">
                What is MixMaster?
            </h2>
            <p class="text-gray-600 text-xl">
                MixMaster is a platform for keeping track of your concrete mix
                designs. You can create, edit, and delete mix designs, as well
                as view all of your mix designs in one place.
            </p>
        </div>
        <div class="flex gap-6">
            <MmCard
                title="Sign in"
                description="Already have an account? Sign in to start keeping track of your concrete mix designs."
            >
                <Button class="bg-primary mt-6" onclick={() => goto("/signin")}
                    >Sign in</Button
                >
            </MmCard>
            <MmCard
                title="Sign up"
                description="Don't have an account yet? Sign up today to start keeping track of your concrete mix designs."
            >
                <Button class="bg-primary mt-6" onclick={() => goto("/signup")}
                    >Sign up</Button
                >
            </MmCard>
        </div>
    </Squeeze>
</Center>
