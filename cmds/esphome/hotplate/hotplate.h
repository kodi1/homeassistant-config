#ifndef __HOTPLATE_H__
#define __HOTPLATE_H__

static lv_obj_t *chart = nullptr;
static lv_chart_series_t *chart_temp_series = nullptr;
static lv_chart_series_t *chart_target_series = nullptr;
static lv_chart_series_t *out_series = nullptr;

void init_chart(lv_obj_t *obj)
{
    chart = lv_chart_create(obj);
    lv_obj_set_size(chart, 370, 240);
    lv_obj_set_pos(chart, 0, 0);
    lv_chart_set_type(chart, LV_CHART_TYPE_LINE);

    // lv_chart_set_update_mode(chart, LV_CHART_UPDATE_MODE_CIRCULAR);
    lv_chart_set_update_mode(chart, LV_CHART_UPDATE_MODE_SHIFT);
    lv_obj_set_style_size(chart, 0, LV_PART_INDICATOR);
    lv_obj_set_style_bg_color(chart, black, LV_PART_MAIN);

    lv_obj_set_style_line_color(chart, gray900, LV_PART_MAIN);
    lv_obj_set_style_line_width(chart, 1, LV_PART_MAIN);
    lv_chart_set_div_line_count(chart, 5, 5);

    lv_chart_set_point_count(chart, 120);

    chart_temp_series = lv_chart_add_series(chart, lv_palette_main(LV_PALETTE_ORANGE), LV_CHART_AXIS_PRIMARY_Y);
    chart_target_series = lv_chart_add_series(chart, lv_palette_main(LV_PALETTE_BLUE_GREY), LV_CHART_AXIS_PRIMARY_Y);
    out_series = lv_chart_add_series(chart, lv_palette_main(LV_PALETTE_GREEN), LV_CHART_AXIS_SECONDARY_Y);
}

/**
 * Calculates and applies the min/max range for a single axis based on multiple series.
 * @param chart The lv_chart object.
 * @param series_list An array of pointers to the series that share this axis.
 * @param num_series The number of series in the array.
 * @param axis The axis to apply the range to (e.g., LV_CHART_AXIS_PRIMARY_Y).
 */
void chart_autoscale_multiple_series(
    lv_obj_t *chart,
    lv_chart_series_t **series_list, // Array of series pointers
    uint8_t num_series,
    lv_chart_axis_t axis)
{
    lv_coord_t overall_min_val = LV_COORD_MAX;
    lv_coord_t overall_max_val = LV_COORD_MIN;
    uint16_t point_count = lv_chart_get_point_count(chart);

    // 1. Iterate through all series provided
    for (uint8_t i = 0; i < num_series; i++) {
        lv_chart_series_t *current_series = series_list[i];

        // Skip null pointers in the list
        if (current_series == NULL) continue;

        // Get the Y-array for the current series
        lv_coord_t *points = lv_chart_get_y_array(chart, current_series);

        // --- Find the min/max values in the current series ---
        for (uint16_t j = 0; j < point_count; j++) {
            // Check for valid points (not LV_CHART_POINT_NONE)
            if (points[j] != LV_CHART_POINT_NONE) {
                if (points[j] < overall_min_val) {
                    overall_min_val = points[j];
                }
                if (points[j] > overall_max_val) {
                    overall_max_val = points[j];
                }
            }
        }
    }

    // Handle the case where no valid points were found across ALL series
    if (overall_min_val == LV_COORD_MAX || overall_max_val == LV_COORD_MIN) {
        // Fallback or keep current range
        return;
    }

    // 2. Add a visual buffer (10% padding)
    lv_coord_t range = overall_max_val - overall_min_val;

    // Calculate 10% buffer. Handle division by zero/zero range.
    lv_coord_t buffer = (range == 0) ? 10 : (range / 10);

    lv_coord_t new_min = overall_min_val - buffer;
    lv_coord_t new_max = overall_max_val + buffer;

    // Ensure range doesn't collapse if all points are the same value
    if (range == 0) {
        new_min = overall_min_val - 1;
        new_max = overall_max_val + 1;
    }

    // 3. Apply the new calculated range to the specified axis
    lv_chart_set_range(chart, axis, new_min, new_max);
}

void update_chart(float target, float current, float out)
{
    lv_chart_series_t *y_series[2];
    uint8_t num_series;
    if (!chart)
        return;

    // Add new data points
    lv_chart_set_next_value(chart, chart_temp_series, current * 10);
    lv_chart_set_next_value(chart, chart_target_series, target * 10);
    lv_chart_set_next_value(chart, out_series, out * 1000);

    y_series[0] = chart_temp_series;
    y_series[1] = chart_target_series;
    num_series = 2;
    chart_autoscale_multiple_series(chart, y_series, num_series, LV_CHART_AXIS_PRIMARY_Y);

    y_series[0] = out_series;
    num_series = 1;
    chart_autoscale_multiple_series(chart, y_series, num_series, LV_CHART_AXIS_SECONDARY_Y);
}

#endif
