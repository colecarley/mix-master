<script>
    import Center from "../../components/center.svelte";
    import Header from "../../components/header.svelte";
    import ProjectForm from "../../components/project-form.svelte";
    import Squeeze from "../../components/squeeze.svelte";
</script>

<Header></Header>
<Center>
    <Squeeze>
        <ProjectForm projectId={null}></ProjectForm>
    </Squeeze>
</Center>
