<script>
    import Center from "../../components/center.svelte";
    import Header from "../../components/header.svelte";
    import MixForm from "../../components/mix-form.svelte";
    import Squeeze from "../../components/squeeze.svelte";
</script>

<Center>
    <Header></Header>
    <Squeeze>
        <h1 class="mb-6 text-gray-600">Create Mix</h1>
        <MixForm mixId={null}></MixForm>
    </Squeeze>
</Center>
