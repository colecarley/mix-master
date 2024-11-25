<script>
    import Center from "../../components/center.svelte";
    import Header from "../../components/header.svelte";
    import ProjectForm from "../../components/project-form.svelte";
    import Squeeze from "../../components/squeeze.svelte";
</script>

<Center>
    <Header></Header>
    <Squeeze>
        <h1 class="mb-6 text-grauy-600">Create Project</h1>
        <ProjectForm projectId={null}></ProjectForm>
    </Squeeze>
</Center>
