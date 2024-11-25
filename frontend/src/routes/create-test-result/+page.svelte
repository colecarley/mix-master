<script lang="ts">
    import Center from "../../components/center.svelte";
    import Header from "../../components/header.svelte";
    import Squeeze from "../../components/squeeze.svelte";
    import TestResultForm from "../../components/test-result-form.svelte";
</script>

<Header></Header>
<Center>
    <Squeeze>
        <h1 class="mb-6">Create Test Result</h1>
        <TestResultForm testResultId={null}></TestResultForm>
    </Squeeze>
</Center>
