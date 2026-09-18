import { BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from "recharts";

import "./CategoryAnalytics.css";

/* --------------------------------
   Custom Tooltip
--------------------------------- */

function ChartTooltip({
  active,
  payload,
  label
}) {
  if (
    !active ||
    !payload ||
    !payload.length
  ) {
    return null;
  }

  const value = payload[0].value;
  const dataKey = payload[0].dataKey;

  const unit =
    dataKey === "hours"
      ? "hours"
      : "tickets";

  return (
    <div className="analytics-tooltip">
      <span className="analytics-tooltip-label">
        {label}
      </span>

      <strong>
        {value} {unit}
      </strong>
    </div>
  );
}

/* --------------------------------
   Empty State
--------------------------------- */

function ChartEmptyState({ message }) {
  return (
    <div className="analytics-chart-empty">
      <span>—</span>
      <p>{message}</p>
    </div>
  );
}

/* --------------------------------
   Main Component
--------------------------------- */

function CategoryAnalytics({
  category,
  sentimentData,
  priorityData,
  statusData,
  resolutionTimeData,
  onFilterSelect
}) {
  const hasSentimentData =
    sentimentData?.some(
      (item) => item.count > 0
    );

  const hasPriorityData =
    priorityData?.some(
      (item) => item.count > 0
    );

  const hasStatusData =
    statusData?.some(
      (item) => item.count > 0
    );

  const hasResolutionData =
    resolutionTimeData?.length > 0;

  /* --------------------------------
     Chart Click Handler
  --------------------------------- */

  const handleChartClick = (data) => {
    const filterValue =
      data?.name ??
      data?.payload?.name;

    if (
      filterValue &&
      typeof onFilterSelect === "function"
    ) {
      onFilterSelect(filterValue);
    }
  };

  return (
    <section className="category-analytics-section">

      {/* --------------------------------
          Section Header
      --------------------------------- */}

      <div className="category-analytics-header">
        <div>
          <span>AI Insights</span>
          <h3>Category Analytics</h3>
          <p>
            Distribution of sentiment, priority,
            status and estimated resolution time
            across {category} tickets.
          </p>
        </div>
      </div>

      {/* --------------------------------
          Analytics Grid
      --------------------------------- */}

      <div className="category-charts-grid">

        {/* =================================
            SENTIMENT
        ================================= */}

        <div className="category-chart-card">

          <div className="category-chart-card-header">
            <div>
              <span className="chart-eyebrow">Customer Experience</span>
              <h4>Sentiment Distribution</h4>
              <p>Click a bar to view matching tickets</p>
            </div>
          </div>

          <div className="category-chart-container">

            {hasSentimentData ? (
              <ResponsiveContainer width="100%" height={280}>
                <BarChart
                  data={sentimentData}
                  margin={{
                    top: 10,
                    right: 10,
                    left: -20,
                    bottom: 5
                  }}
                >

                <CartesianGrid
                  strokeDasharray="3 3"
                  vertical={false}
                />

                <XAxis
                  dataKey="name"
                  tickLine={false}
                  axisLine={false}
                />

                <YAxis
                  allowDecimals={false}
                  tickLine={false}
                  axisLine={false}
                />

                <Tooltip
                  cursor={{
                    fill: "rgba(99, 91, 255, 0.05)"
                    }}
                    content={
                      <ChartTooltip />
                    }
                  />

                  <Bar
                    dataKey="count"
                    name="Tickets"
                    fill="#635bff"
                    radius={[8, 8, 0, 0]}
                    maxBarSize={58}
                    onClick={handleChartClick}
                    cursor="pointer"
                  />

                </BarChart>
              </ResponsiveContainer>
            ) : (
              <ChartEmptyState
                message="No sentiment data available."
              />
            )}

          </div>
        </div>

        {/* =================================
            PRIORITY
        ================================= */}

        <div className="category-chart-card">

          <div className="category-chart-card-header">
            <div>
              <span className="chart-eyebrow">Ticket Urgency</span>
              <h4>Priority Distribution</h4>
              <p>Click a bar to view matching tickets</p>
            </div>
          </div>

          <div className="category-chart-container">

            {hasPriorityData ? (
              <ResponsiveContainer width="100%" height={280}
              >
                <BarChart
                  data={priorityData}
                  margin={{top: 10, right: 10, left: -20, bottom: 5}}
                >

                  <CartesianGrid
                    strokeDasharray="3 3"
                    vertical={false}
                  />

                  <XAxis
                    dataKey="name"
                    tickLine={false}
                    axisLine={false}
                  />

                  <YAxis
                    allowDecimals={false}
                    tickLine={false}
                    axisLine={false}
                  />

                  <Tooltip
                    cursor={{
                      fill:"rgba(247, 144, 9, 0.05)"
                    }}
                    content={
                      <ChartTooltip />
                    }
                  />

                  <Bar
                  dataKey="count"
                    name="Tickets"
                    fill="#f79009"
                    radius={[8,8,0,0]}
                    maxBarSize={58}
                    onClick={handleChartClick}
                    cursor="pointer"
                  />

                </BarChart>
              </ResponsiveContainer>
            ) : (
              <ChartEmptyState
                message="No priority data available."
              />
            )}

          </div>
        </div>

        {/* =================================
            STATUS
        ================================= */}

        <div className="category-chart-card">

          <div className="category-chart-card-header">
            <div>
              <span className="chart-eyebrow">Ticket Workflow</span>
              <h4>Ticket Status</h4>
              <p>Click a bar to view matching tickets</p>
            </div>
          </div>

          <div className="category-chart-container">

            {hasStatusData ? (
              <ResponsiveContainer width="100%" height={280}>
                <BarChart
                  data={statusData}
                  margin={{
                    top: 10,
                    right: 10,
                    left: -20,
                    bottom: 5
                  }}
                >

                  <CartesianGrid
                    strokeDasharray="3 3"
                    vertical={false}
                  />

                  <XAxis
                    dataKey="name"
                    tickLine={false}
                    axisLine={false}
                  />

                  <YAxis
                    allowDecimals={false}
                    tickLine={false}
                    axisLine={false}
                  />

                  <Tooltip
                    cursor={{
                      fill:"rgba(18, 183, 106, 0.05)"}}
                    content={
                      <ChartTooltip />
                    }
                  />

                  <Bar
                    dataKey="count"
                    name="Tickets"
                    fill="#12b76a"
                    radius={[8, 8, 0, 0]}
                    maxBarSize={58}
                    onClick={handleChartClick}
                    cursor="pointer"
                  />

                </BarChart>
              </ResponsiveContainer>
            ) : (
              <ChartEmptyState
                message="No status data available."
              />
            )}

          </div>
        </div>

        {/* =================================
            RESOLUTION TIME
        ================================= */}

        <div className="category-chart-card">

          <div className="category-chart-card-header">
            <div>
              <span className="chart-eyebrow">AI Prediction</span>
              <h4>Resolution Time</h4>
              <p>Estimated resolution time per ticket</p>
            </div>
          </div>

          <div className="category-chart-container">

            {hasResolutionData ? (
              <ResponsiveContainer width="100%" height={280} >
                <LineChart
                  data={resolutionTimeData}
                  margin={{
                    top: 10,
                    right: 10,
                    left: -20,
                    bottom: 5
                  }}
                >

                  <CartesianGrid
                    strokeDasharray="3 3"
                    vertical={false}
                  />

                  <XAxis
                    dataKey="name"
                    tickLine={false}
                    axisLine={false}
                  />

                  <YAxis
                    allowDecimals={false}
                    tickLine={false}
                    axisLine={false}
                    label={{
                      value: "Hours",
                      angle: -90,
                      position: "insideLeft"
                    }}
                  />

                  <Tooltip
                    cursor={{
                      stroke: "#635bff",
                      strokeWidth: 1
                    }}
                    content={
                      <ChartTooltip />
                    }
                  />

                  <Line
                    type="monotone"
                    dataKey="hours"
                    name="Hours"
                    stroke="#635bff"
                    strokeWidth={3}
                    dot={{
                      r: 4
                    }}
                    activeDot={{
                      r: 6
                    }}
                  />

                </LineChart>
              </ResponsiveContainer>
            ) : (
              <ChartEmptyState
                message="No resolution data available."
              />
            )}

          </div>
        </div>

      </div>
    </section>
  );
}

export default CategoryAnalytics;

