<script>
    import Center from "../../components/center.svelte";
    import Header from "../../components/header.svelte";
    import MixForm from "../../components/mix-form.svelte";
    import Squeeze from "../../components/squeeze.svelte";
</script>

<Header></Header>
<Center>
    <Squeeze>
        <MixForm mixId={null}></MixForm>
    </Squeeze>
</Center>
