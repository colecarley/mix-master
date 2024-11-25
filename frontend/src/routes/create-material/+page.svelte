<script>
    import Center from "../../components/center.svelte";
    import Header from "../../components/header.svelte";
    import MaterialForm from "../../components/material-form.svelte";
    import Squeeze from "../../components/squeeze.svelte";
</script>

<Header></Header>
<Center>
    <Squeeze>
        <MaterialForm materialId={null} proportionId={null}></MaterialForm>
    </Squeeze>
</Center>
