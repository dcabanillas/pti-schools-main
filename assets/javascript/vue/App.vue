<template>
  <div class="columns">
    <div class="column is-half">
      <div class="panel is-primary">
        <p class="panel-heading">Exercise 1</p>
        <div class="block p-4">
          <p>Create a variable named "x" that contains an integer value</p>
          <br />
          <div class="columns">
            <div class="column">
              <div class="control" :class="{ 'is-loading': isLoading }">
                <textarea
                  class="textarea"
                  id="exercise_1"
                  v-model="exercise[1]"
                  @click="() => activate(1)"
                  rows="3"
                ></textarea>
              </div>
            </div>
          </div>
          <div class="columns">
            <div class="column">
              <button
                class="button is-info is-large is-fullwidth"
                @click="() => run(1)"
              >
                Run
              </button>
            </div>
            <div class="column">
              <button
                class="button is-success is-large is-fullwidth"
                @click="() => save(1)"
              >
                Save
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="column is-half">
      <div class="panel is-warning">
        <p class="panel-heading">Solution 1</p>
        <div class="block p-4">
          <p>Your code will be executed below</p>
          <br />
          <div class="columns">
            <div class="column">
              <div class="control" :class="{ 'is-loading': isLoading }">
                <textarea
                  class="textarea"
                  id="solution_1"
                  disabled
                  v-model="solution[1]"
                  rows="3"
                ></textarea>
              </div>
            </div>
          </div>
          <div class="columns">
            <div class="column">
              <button
                class="button is-info is-large is-fullwidth"
                @click="() => clean(1)"
              >
                Clean
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <br />
  <div class="columns">
    <div class="column is-half">
      <div class="panel is-primary">
        <p class="panel-heading">Exercise 2</p>
        <div class="block p-4">
          <p>Create 2 numeric variables, add them and show the result</p>
          <br />
          <div class="columns">
            <div class="column">
              <div class="control" :class="{ 'is-loading': isLoading }">
                <textarea
                  class="textarea"
                  id="exercise_2"
                  v-model="exercise[2]"
                  @click="() => activate(2)"
                  rows="3"
                ></textarea>
              </div>
            </div>
          </div>
          <div class="columns">
            <div class="column">
              <button
                class="button is-info is-large is-fullwidth"
                @click="() => run(2)"
              >
                Run
              </button>
            </div>
            <div class="column">
              <button
                class="button is-success is-large is-fullwidth"
                @click="() => save(2)"
              >
                Save
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="column is-half">
      <div class="panel is-warning">
        <p class="panel-heading">Solution 2</p>
        <div class="block p-4">
          <p>Your code will be executed below</p>
          <br />
          <div class="columns">
            <div class="column">
              <div class="control" :class="{ 'is-loading': isLoading }">
                <textarea
                  class="textarea"
                  id="solution_1"
                  disabled
                  v-model="solution[2]"
                  rows="3"
                ></textarea>
              </div>
            </div>
          </div>
          <div class="columns">
            <div class="column">
              <button
                class="button is-info is-large is-fullwidth"
                @click="() => clean(2)"
              >
                Clean
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      isLoading: true,
      number_active: 1,
      exercise: { 1: null, 2: null },
      solution: { 1: null, 2: null },
      pyodide: null,
      stdoutBuffer: new Array(),
      stderrBuffer: new Array(),
    };
  },
  computed: {
    active: {
      get: function () {
        return this.number_active;
      },
      set: function (newValue) {
        this.number_active = newValue;
      },
    },
    exercises: {
      get: function () {
        return this.exercise;
      },
      set: function (newValue) {
        this.exercise = newValue;
      },
    },
    solutions: {
      get: function () {
        return this.solution;
      },
      set: function (newValue) {
        this.solution = newValue;
      },
    },
  },
  methods: {
    stdout: function (msg) {
      this.stdoutBuffer.push(msg);
      this.toOutput();
    },
    stderr: function (msg) {
      this.stderrBuffer.push(msg);
      this.toOutput();
    },
    toOutput: function () {
      let code = this.exercises[this.active];
      let splittedCode = code.split("\n");
      let output = ">>>";

      splittedCode.forEach((c) => {
        if (c.startsWith(" ")) {
          output += "...\t" + c + "\n";
        } else {
          output += c + "\n";
        }
      });

      this.stdoutBuffer.forEach((m) => {
        output += m + "\n";
      });

      this.solutions[this.active] = output;
    },
    initializePyodide: async function () {
      try {
        this.pyodide = await window.loadPyodide({
          indexURL: "https://cdn.jsdelivr.net/pyodide/v0.19.1/full/",
          stdout: this.stdout,
          stderr: this.stderr,
        });
        this.loaded();
      } catch (error) {
        this.errorLoading(error);
      }
    },
    save: function (number) {
      console.log("save");
    },
    activate: function (number) {
      this.active = number;
    },
    clean: function () {
      this.exercises = {
        1: "print('Your code goes here')",
        2: "print('Your code goes here')",
      };
      this.solutions = { 1: ">>>", 2: ">>>" };
    },
    cleanBuffers: function () {
      this.stdoutBuffer = new Array();
      this.stderrBuffer = new Array();
    },
    run: function (number) {
      this.activate(number);
      this.cleanBuffers();

      let code = this.exercises[this.active];
      let out = this.pyodide.runPython(code);

      if (out !== undefined) {
        this.stdout(out);
      }
    },
    loaded: function () {
      this.isLoading = false;
      this.clean();
      this.cleanBuffers();
    },
    errorLoading: function (error) {
      this.isLoading = false;
      this.solution = { 1: error, 2: error };
    },
  },
  created: async function () {
    let loading = "Loading...";
    this.exercises = {
      1: loading,
      2: loading,
    };
    this.solutions = { 1: loading, 2: loading };
    await this.initializePyodide();
  },
};
</script>
