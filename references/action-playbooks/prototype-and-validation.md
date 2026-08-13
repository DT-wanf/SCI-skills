# Prototype and Validation

Use when a method/application paper requires code, a runnable prototype, simulation, hardware, user testing, case validation, or benchmark experiments.

## Capability decision

If the agent has access to the code workspace and the task is authorized, it may implement and test software. Switch to manual or hybrid when execution requires:

- local private data not uploaded;
- specialized hardware or instruments;
- human participants;
- paid or authenticated platforms;
- production systems;
- physical environments.

## Before building

Lock:

- problem and user scenario;
- minimum viable functions;
- inputs and outputs;
- baseline or competing solution;
- success metrics and thresholds;
- test dataset or cases;
- resource limits;
- failure and safety conditions.

## Operation guide

Give numbered steps for:

1. environment setup;
2. dependency and version recording;
3. data or input preparation;
4. minimum implementation;
5. smoke test;
6. baseline run;
7. main run;
8. error and exception logging;
9. ablation or sensitivity checks;
10. artifact export.

## Completion evidence

Request:

- source code or configuration;
- environment file;
- run command;
- console logs;
- test report;
- outputs and figures;
- baseline comparison;
- known failures;
- human or hardware test records where applicable.

Do not treat code compilation or a single successful run as full validation.
