import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer
} from "recharts";

import "./CategoryAnalytics.css";

function CategoryAnalytics({
  category,
  sentimentData,
  priorityData,
  statusData,
  resolutionTimeData
}) {
  return (
    <section className="category-analytics-section">

      {/* Section Header */}

      <div className="category-analytics-header">

        <div>

          <span>
            AI Insights
          </span>

          <h3>
            Category Analytics
          </h3>

          <p>
            Distribution of sentiment, priority,
            status and resolution time across{" "}
            {category} tickets.
          </p>

        </div>

      </div>


      {/* Charts */}

      <div className="category-charts-grid">

        {/* Sentiment */}

        <div className="category-chart-card">

          <div className="category-chart-card-header">

            <div>

              <h4>
                Sentiment Distribution
              </h4>

              <p>
                Customer emotional tone
              </p>

            </div>

          </div>


          <div className="category-chart-container">

            <ResponsiveContainer
              width="100%"
              height={280}
            >

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
                />

                <YAxis
                  allowDecimals={false}
                />

                <Tooltip />

                <Bar
                  dataKey="count"
                  name="Tickets"
                  radius={[
                    7,
                    7,
                    0,
                    0
                  ]}
                />

              </BarChart>

            </ResponsiveContainer>

          </div>

        </div>


        {/* Priority */}

        <div className="category-chart-card">

          <div className="category-chart-card-header">

            <div>

              <h4>
                Priority Distribution
              </h4>

              <p>
                Ticket urgency levels
              </p>

            </div>

          </div>


          <div className="category-chart-container">

            <ResponsiveContainer
              width="100%"
              height={280}
            >

              <BarChart
                data={priorityData}
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
                />

                <YAxis
                  allowDecimals={false}
                />

                <Tooltip />

                <Bar
                  dataKey="count"
                  name="Tickets"
                  radius={[
                    7,
                    7,
                    0,
                    0
                  ]}
                />

              </BarChart>

            </ResponsiveContainer>

          </div>

        </div>


        {/* Status */}

        <div className="category-chart-card">

          <div className="category-chart-card-header">

            <div>

              <h4>
                Ticket Status
              </h4>

              <p>
                Current status of category tickets
              </p>

            </div>

          </div>


          <div className="category-chart-container">

            <ResponsiveContainer
              width="100%"
              height={280}
            >

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
                />

                <YAxis
                  allowDecimals={false}
                />

                <Tooltip />

                <Bar
                  dataKey="count"
                  name="Tickets"
                  radius={[
                    7,
                    7,
                    0,
                    0
                  ]}
                />

              </BarChart>

            </ResponsiveContainer>

          </div>

        </div>


        {/* Resolution Time */}

        <div className="category-chart-card">

          <div className="category-chart-card-header">

            <div>

              <h4>
                Resolution Time
              </h4>

              <p>
                Estimated resolution time per ticket
              </p>

            </div>

          </div>


          <div className="category-chart-container">

            <ResponsiveContainer
              width="100%"
              height={280}
            >

              <BarChart
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
                />

                <YAxis
                  allowDecimals={false}
                  label={{
                    value: "Hours",
                    angle: -90,
                    position: "insideLeft"
                  }}
                />

                <Tooltip />

                <Bar
                  dataKey="hours"
                  name="Hours"
                  radius={[
                    7,
                    7,
                    0,
                    0
                  ]}
                />

              </BarChart>

            </ResponsiveContainer>

          </div>

        </div>

      </div>

    </section>
  );
}

export default CategoryAnalytics;

