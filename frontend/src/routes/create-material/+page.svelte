<script>
    import Center from "../../components/center.svelte";
    import Header from "../../components/header.svelte";
    import MaterialForm from "../../components/material-form.svelte";
    import Squeeze from "../../components/squeeze.svelte";
</script>

<Header></Header>
<Center>
    <Squeeze>
        <h1 class="mb-6">Create Material</h1>
        <MaterialForm materialId={null} proportionId={null}></MaterialForm>
    </Squeeze>
</Center>
